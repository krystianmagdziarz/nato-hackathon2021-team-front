import {Tag} from "antd";
import React from "react";

export default function DescInfo({hospitalCapabilities}) {
    const descEntries = !hospitalCapabilities ? null : Object.entries(hospitalCapabilities);

    if (!descEntries) return null;

    return (
        <div style={{textAlign: 'start', marginTop: '24px'}}>
            <div style={{flexFlow: 'row wrap', marginTop: '12px', maxWidth: '600px'}}>
                {
                    descEntries.map(item => {
                        if (item[0] !== 'id' && item[1] !== 'type') {
                            return <Tag key={item[0]}
                                        style={{marginTop: '12px', minHeight: '40px', display: 'inline-flex', flexDirection: 'center', alignItems: 'center', paddingLeft: '12px', paddingRight: '12px', textTransform: 'capitalize'}}>{
                                            item[0].replaceAll("_", " ")}
                            </Tag>
                        }
                    })
                }
            </div>
        </div>
    );
}