from rest_framework.decorators import api_view
from rest_framework.response import Response

from neo4jintegration.serializers import PointsSerializer

from neo4j import GraphDatabase


class Neo4jHackathon:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def do_command(self, command):
        with self.driver.session() as session:
            result = session.write_transaction(self._do_command_result, command)
            print(result)

    @staticmethod
    def _do_command_result(tx, command):
        result = tx.run(command)
        return result.single()

    def calculate_shortest_path(self, node1, node2):
        with self.driver.session() as session:
            result = session.write_transaction(self._get_shortest_path_static, node1, node2)
            return result

    @staticmethod
    def _get_shortest_path_static(tx, node1, node2):
        result = tx.run("MATCH (source:Grid {name: '%s'}), (target:Grid {name: '%s'}) CALL gds.beta.shortestPath.astar.stream('mapGraph', { sourceNode: id(source), targetNode: id(target), latitudeProperty: 'latitude', longitudeProperty: 'longitude', relationshipWeightProperty: 'distance' }) YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs RETURN index, gds.util.asNode(sourceNode).name AS sourceNodeName, gds.util.asNode(targetNode).name AS targetNodeName, totalCost, [nodeId IN nodeIds | gds.util.asNode(nodeId).name] AS nodeNames, costs ORDER BY index" % (node1, node2))
        # print(result)
        return result.single()

    def shortest_path_time(self, node1, node2):
        with self.driver.session() as session:
            result = session.write_transaction(self._get_shortest_path_time_result, node1, node2)
            return result

    @staticmethod
    def _get_shortest_path_time_result(tx, node1, node2):
        result = tx.run("MATCH (source:Grid {name: '%s'}), (target:Grid {name: '%s'}) CALL gds.beta.shortestPath.astar.stream('mapGraph', { sourceNode: id(source), targetNode: id(target), latitudeProperty: 'latitude', longitudeProperty: 'longitude', relationshipWeightProperty: 'time' }) YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs RETURN index, gds.util.asNode(sourceNode).name AS sourceNodeName, gds.util.asNode(targetNode).name AS targetNodeName, totalCost, [nodeId IN nodeIds | gds.util.asNode(nodeId).name] AS nodeNames, costs ORDER BY index" % (node1, node2))
        # print(result)
        return result.single()


    def get_single_node(self, node1):
        with self.driver.session() as session:
            result = session.write_transaction(self._get_single_node_result, node1)
            return result

    @staticmethod
    def _get_single_node_result(tx, node1):
        result = tx.run("Match (n:Grid{name: '%s'})-[r]->(m:Grid) Return m.name AS nodeNames" % node1)
        n_nodes = []
        for x in result:
            n_nodes.append(x["nodeNames"])
        return n_nodes

    def update_node_value(self, node1, node2, distance):
        with self.driver.session() as session:
            result = session.write_transaction(self._update_node_value_result, node1, node2, distance)
            return result

    @staticmethod
    def _update_node_value_result(tx, node1, node2, distance):
        result1 = tx.run("MATCH (:Grid {name: '%s'})-[rel:CONNECTION]->(:Grid {name: '%s'}) SET rel.distance = %s "
                        "RETURN rel" % (node1, node2, distance))
        result2 = tx.run("MATCH (:Grid {name: '%s'})-[rel:CONNECTION]->(:Grid {name: '%s'}) SET rel.distance = %s "
                        "RETURN rel" % (node2, node1, distance))
        return result1, result2

    def remove_graph(self):
        with self.driver.session() as session:
            result = session.write_transaction(self._remove_graph_result)
            return result

    @staticmethod
    def _remove_graph_result(tx):
        result = tx.run("CALL gds.graph.drop('mapGraph')")
        return result.single()

    def create_new_graph(self):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_new_graph_result)
            return result

    @staticmethod
    def _create_new_graph_result(tx):
        result = tx.run("CALL gds.graph.create( 'mapGraph', 'Grid', 'CONNECTION', { nodeProperties: ['latitude', 'longitude'], relationshipProperties: ['distance', 'time'] })")
        return result.single()

# ----


def calculate_shortest_path_time(node1, node2):
    greeter = Neo4jHackathon("bolt://neo4jhackathon:7687", "neo4j", "test")
    result = greeter.shortest_path_time(node1, node2)
    greeter.close()
    return result


def calculate_shortest_node_path(node1, node2):
    greeter = Neo4jHackathon("bolt://neo4jhackathon:7687", "neo4j", "test")
    result = greeter.calculate_shortest_path(node1, node2)
    greeter.close()
    return result


def update_node_value_method(node1, distance):
    greeter = Neo4jHackathon("bolt://neo4jhackathon:7687", "neo4j", "test")
    # Get node
    result = greeter.get_single_node(node1)
    # Update edges
    for x in result:
        greeter.update_node_value(node1, x, distance)
    # Remove graph
    greeter.remove_graph()
    # Create new graph
    greeter.create_new_graph()
    # Close
    greeter.close()
    return result

# ----


@api_view(["GET"])
def neo4j_shortest_path(request, node1, node2):
    points = calculate_shortest_node_path(node1, node2)
    serializer = PointsSerializer({
        "points": points["nodeNames"]
    })
    return Response(serializer.data)


@api_view(["GET"])
def neo4j_shortest_path_time(request, node1, node2):
    points = calculate_shortest_path_time(node1, node2)
    serializer = PointsSerializer({
        "points": points["nodeNames"]
    })
    return Response(serializer.data)


@api_view(["GET"])
def neo4j_update_node_value(request, node1, distance):
    nodes = update_node_value_method(node1, distance)
    serializer = PointsSerializer({
        "points": nodes
    })
    return Response(serializer.data)

