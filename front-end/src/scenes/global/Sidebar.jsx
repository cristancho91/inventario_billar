import { useState } from "react";
import { Sidebar, Menu, MenuItem, sidebarClasses, menuClasses } from 'react-pro-sidebar';
import { Box, IconButton, Typography, menuItemClasses, useTheme } from "@mui/material";
import { Item } from "./Item";
import { tokens } from "../../theme";
import HomeOutlinedIcon from "@mui/icons-material/HomeOutlined";
import PeopleOutlinedIcon from "@mui/icons-material/PeopleOutlined";
import ContactsOutlinedIcon from "@mui/icons-material/ContactsOutlined";
import ReceiptOutlinedIcon from '@mui/icons-material/ReceiptOutlined';
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";
import CalendarTodayOutlinedIcon from "@mui/icons-material/CalendarTodayOutlined";
import HelpOutlinedIcon from "@mui/icons-material/HelpOutlined";
import BarChartOutlinedIcon from "@mui/icons-material/BarChartOutlined";
import PieChartOutlineOutlinedIcon from '@mui/icons-material/PieChartOutlineOutlined';
import TimelineOutlinedIcon from '@mui/icons-material/TimelineOutlined';
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";
import MapOutlinedIcon from "@mui/icons-material/MapOutlined";


export const Sidebars = ()=>{
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const [isCollapsed, setisCollapsed ] = useState(false);
    const [selected, setSelected] = useState("Inicio");

    return (
        <Box >

            {/* sidebar */}
            <Sidebar collapsed={ isCollapsed } 
                style={{
                    borderColor:"transparent",
                }}
                rootStyles={
                    {
                        [`.${sidebarClasses.container}`]: {
                            backgroundColor: `${colors.primary[400]}`,
                          },
                          [`.${menuClasses.button}:hover`]: {
                            color: "#868dfb !important",
                            background: `${colors.primary[400]}  !important`
                          },
                          [`.${menuItemClasses.selected}`]: {
                            color: "#868dfb !important",
                            background: `${colors.primary[600]}  !important`
                          },
                          
                    }
                }
                
            >
                <Menu iconShape="square" 
                
                   menuItemStyles={
                    {
                        button: {
                            // the active class will be added automatically by react router
                            // so we can use it to style the active menu item
                            [`&.ps-active`]: {
                              color: "#868dfb !important",
                            },
                        },
                    }
                   }
                >
                    {/* LOGO AND MENU ICON  */}
                    <MenuItem  
                    onClick={()=> setisCollapsed(!isCollapsed)}
                    icon ={isCollapsed ? <MenuOutlinedIcon /> : undefined}
                    style={{
                        margin: "10px 0 20px 0",
                        color: colors.grey[100],
                      }}
                    >
                        {!isCollapsed && (
                            <Box 
                            display="flex"
                            justifyContent="space-between"
                            alignItems="center"
                            ml="15px">
                                <Typography variant='h3'>
                                    B. DAYTONA
                                </Typography>
                                <IconButton onClick={()=> setisCollapsed(!isCollapsed)}>
                                    <MenuOutlinedIcon />
                                </IconButton>

                            </Box>
                        )}

                    </MenuItem> 
                    {
                        !isCollapsed && (
                            <Box mb="25px">
                                <Box display="flex" justifyContent="center" alignItems="center">
                                    <img alt="profile-user"
                                    width="100px"
                                    height="100px"
                                    src={`../../assets/user.png`}
                                    style={{ cursor: "pointer", borderRadius: "50%" }} />

                                </Box>
                                <Box textAlign="center">
                                <Typography
                                variant="h2"
                                color={colors.grey[100]}
                                fontWeight="bold"
                                sx={{ m: "10px 0 0 0" }}
                                >
                                Ed Roh
                                </Typography>
                                <Typography variant="h5" color={colors.greenAccent[500]}>
                                Administrador
                                </Typography>
                            </Box>
                            </Box>
                        )}
                         <Box paddingLeft={isCollapsed ? undefined : "10%"}>
                        <Item
                        title="Inicio"
                        to="/"
                        icon={<HomeOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />

                        <Typography
                        variant="h6"
                        color={colors.grey[100]}
                        sx={{ m: "15px 0 5px 20px" }}
                        >
                        Datos
                        </Typography>

                        <Item
                        title="Usuarios"
                        to="/team"
                        icon={<PeopleOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />
                        <Item
                        title="Contacts Information"
                        to="/contacts"
                        icon={<ContactsOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />
                        <Item
                        title="Invoices Balances"
                        to="/invoices"
                        icon={<ReceiptOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />

                        <Typography
                        variant="h6"
                        color={colors.grey[100]}
                        sx={{ m: "15px 0 5px 20px" }}
                        >
                        Pages
                        </Typography>
                        <Item
                        title="Profile Form"
                        to="/form"
                        icon={<PersonOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />
                        <Item
                        title="Calendar"
                        to="/calendar"
                        icon={<CalendarTodayOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />
                        <Item
                        title="FAQ Page"
                        to="/faq"
                        icon={<HelpOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />

                        <Typography
                        variant="h6"
                        color={colors.grey[100]}
                        sx={{ m: "15px 0 5px 20px" }}
                        >
                        Charts
                        </Typography>
                        <Item
                        title="Bar Chart"
                        to="/bar"
                        icon={<BarChartOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />
                        <Item
                        title="Pie Chart"
                        to="/pie"
                        icon={<PieChartOutlineOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />
                        <Item
                        title="Line Chart"
                        to="/line"
                        icon={<TimelineOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />
                        <Item
                        title="Geography Chart"
                        to="/geography"
                        icon={<MapOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                        />
                    </Box>
                </Menu>
            </Sidebar>
        </Box>
    )

}