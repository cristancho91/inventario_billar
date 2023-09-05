import { Box,Typography, useTheme } from "@mui/material";
import {DataGrid} from "@mui/x-data-grid";
import { tokens } from "../../theme";
import {mockDataTeam} from "../../data/mockData";
import AdminPanelSettingsOutlinedIcon from '@mui/icons-material/AdminPanelSettingsOutlined';
import LockOpenOutlinedIcon from '@mui/icons-material/LockOpenOutlined';
import SecurityOutlinedIcon from '@mui/icons-material/SecurityOutlined';
import { Header } from "../../components/Header";


export const Team=()=>{
    const theme = useTheme();

    const colors = tokens(theme.palette.mode);

    const columns = [
        {
        field: "id",headerName:"ID"
    },
    {
        field:"name", 
        headerName:"Nombre", 
        flex: 1,
        cellClassName:"name-column--cell"
    },
    {
        field:"email", 
        headerName:"Correo",
        flex: 1,
    },
    {
        field:"age",
        headerName:"Edad",
        type:"number",
        headerAlign:"left",
        align:"left",
    },
    {
        field:'phone', 
        headerName:"Telefono",
        flex: 1,
    },
    {
        field:"access", 
        headerName:"Access Level",
        flex:1,
        renderCell: ({row:{access}}) =>{
            return(
                <Box 
                width="60%"
                m="0 auto"
                p="5px"
                display="flex"
                justifyContent="center"
                alignItems="center"
                backgroundColor= {
                    access === 'admin' 
                    ? `${colors.greenAccent[600]}` 
                    : `${colors.greenAccent[700]}`

                }
                borderRadius="4px"


                >
                    { access === "admin" && <AdminPanelSettingsOutlinedIcon /> }                    
                    { access === "manager" && <SecurityOutlinedIcon /> }
                    { access === "user" && <LockOpenOutlinedIcon /> }
                    <Typography  color={colors.grey[100]} sx={{ml:"5px"}}>{access}</Typography>

                </Box>
            )

        }
    }
]

    return (
        <Box m="20px">
            <Header title="TEAM" subtitle="Managing the Team members"/>

            <Box 
            ml="40px"
            height="75vh"
            sx={{
                "& .MuiDataGrid-root":{
                    border:"none"
                },
                "& .MuiDataGrid-cell":{
                    border: "none"
                },
                "& .name-column--cell":{
                    color: colors.greenAccent[500]
                },
                "& .MuiDataGrid-columnHeaders":{
                    backgroundColor: colors.blueAccent[700],
                    borderBottom:"none"
                },
                "& .MuiDataGrid-virtualScroller":{
                    backgroundColor: colors.primary[400]
                },
                "& .MuiDataGrid-footerContainer":{
                    borderTop:"none",
                    backgroundColor: colors.blueAccent[700]
                },
                 "& .MuiCheckbox-root":{
                    color: `${colors.greenAccent[200]} !important`
                },
                
            }}
            >
                <DataGrid 
                    checkboxSelection
                    rows={mockDataTeam}
                    columns={columns}
                />
            </Box>
        </Box>
    )

}