import React, {useState, useContext} from 'react';
import {Card, Switch, Tabs} from 'antd';
import AddObjectPanel from "./addObjectPanel";
import InformationPanel from "./informationPanel";
import {DataContext} from "../../../dataContext";


export default function MapPanel({clickPoint, setClickPoint, ...props}) {
    const { simulation, setSimulation } = useContext(DataContext);
    const [selectedTab, setSelectedTab] = useState();


    const tabItems = [
        {
            title: 'Information',
            content: <InformationPanel/>,
        },
        {
            title: 'Test data',
            content: <AddObjectPanel/>,
        }
    ]

    return (
        <div {...props}>
            <Card style={{height: '100%', overflow: 'auto'}}>
                <Tabs value={selectedTab} onChange={setSelectedTab}
                      tabBarExtraContent={(
                          <div style={{display: 'flex', flexDirection: 'row', alignItems: 'center'}}>
                              <div style={{marginRight: '16px', fontWeight: '600'}}>Route simulation</div>
                              <Switch checked={simulation} onChange={(simulation) => {
                                  setSimulation(simulation);
                              }} />
                          </div>
                      )}
                >
                    {
                        tabItems.map(({title, content}) => (
                            <Tabs.TabPane key={title} tab={title}>
                                {content}
                            </Tabs.TabPane>
                        ))
                    }
                </Tabs>
            </Card>
        </div>
    );
}