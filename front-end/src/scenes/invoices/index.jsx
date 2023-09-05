import { Box,Typography, useTheme } from "@mui/material";
import {DataGrid, GridToolbar} from "@mui/x-data-grid";
import { tokens } from "../../theme";
import {mockDataInvoices} from "../../data/mockData";
import { Header } from "../../components/Header";


export const Invoices=()=>{
    const theme = useTheme();

    const colors = tokens(theme.palette.mode);

    const columns = [
        {
        field: "id",headerName:"ID",flex: 0.5
    },
    {
        field:"name", 
        headerName:"Nombre", 
        flex: 1,
        cellClassName:"name-column--cell"
    },
    {
        field:'phone', 
        headerName:"Telefono",
        flex: 1,
    },
    {
        field:"email", 
        headerName:"Correo",
        flex: 1,
    },
    {
        field:"cost",
        headerName:"Precio",
        renderCell: (params) => (
            <Typography color={colors.greenAccent[500]}>
              ${params.row.cost}
            </Typography>
          ),
        
    },
    
    {
        field:"date", 
        headerName:"Fecha",
        flex:1
    }
]

    return (
        <Box m="20px">
            <Header title="INVOICES" subtitle="List the Invoices Balance"/>

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
                "& .MuiDataGrid-toolbarContainer .MuiButton-text":{
                    color: `${colors.grey[100]}`
                },
                "& .MuiCheckbox-root":{
                    color: `${colors.greenAccent[200]} !important`
                },
                
            }}
            >
                <DataGrid 
                    checkboxSelection
                    rows={mockDataInvoices}
                    columns={columns}
                    slots={{
                        toolbar: GridToolbar,
                      }}
                />
            </Box>
        </Box>
    )

}