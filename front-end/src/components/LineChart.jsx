import { useTheme } from "@mui/material";
import { ResponsiveLine } from "@nivo/line";
import { tokens } from "../theme";
import { mockLineData } from "../data/mockData";
import PropTypes from 'prop-types';




export const LineChart = ({isDashboard =false}) => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode)

    return(
        <ResponsiveLine
        data={mockLineData}
        theme={
            {
                axis: {
                    domain:{
                        line:{
                            stroke:colors.grey[100]
                        },
                    },
                    legend:{
                        text:{
                            fill:colors.grey[100],
                        },
                    },
                    ticks:{
                        line:{
                            strokeWidth: 1,
                            stroke:colors.grey[100],
                        },
                        text:{
                            fill: colors.grey[100],
                        },
                    },
                    
                },
                legends:{
                    text:{
                        fill: colors.grey[100],
                    },
                },
                tooltip:{
                    container: {
                        color: colors.primary[500],
                    },
                },
            }
        }
        colors={isDashboard ? {datum:"color"} : {scheme:"nivo"}}
        margin={{top:50,right:110,bottom:50,left:60}}
        xScale={{type:"point"}}
        yScale={{type:"linear",stacked:true,min:"auto",max:"auto", reverse:false,}}
        yFormat=" >-.2f"
        curve="catmullRom"
        axisTop={null}
        axisRight={null}
        axisBottom={{
            orient:"bottom",
            tickSize:0,
            tickPadding:5,
            tickRotation:0,
            legendPosition:'middle',
            legendOffset:36,
            legend: isDashboard ? undefined : "trasportation",
        }}
        axisLeft={{
            orient:"left",
            tickSize:3,
            tickPadding:5,
            tickRotation:0,
            legendPosition:'middle',
            legendOffset:-40,
            legend: isDashboard ? undefined : "count",
            tickValues:5,
        }}
        enableGridX={false}
        enableGridY={false}
        pointSize={8}
        pointBorderWidth={2}
        pointColor={{theme: "background"}}
        pointLabelYOffset={-12}
        pointBorderColor={{from: "serieColor"}}
        useMesh={true}
        legends={[
            {
                anchor: "bottom-right",
                direction: "column",
                justify: false,
                translateX: 100,
                translateY: 0,
                itemsSpacing: 0,
                itemDirection: "left-to-right",
                itemWidth: 80,
                itemHeight:20,
                itemOpacity: 0.75,
                symbolShape: "circle",
                symbolSize: 12,
                symbolBorderColor: "rgba(0,0,0,.5)",
                effects:[
                    {
                        on: "hover",
                        style:{
                            itemBackground:"rgba(0,0,0,.03)",
                            itemOpacity:1,
                        },
                    },
                ],
            },
        ]}
        
        />

    )
}

LineChart.propTypes={
    isDashboard: PropTypes.bool,
}