import {MenuItem } from 'react-pro-sidebar';
import { Typography,useTheme } from "@mui/material";
import { tokens } from '../../theme';
import { Link } from "react-router-dom";
import PropTypes from 'prop-types';




export const Item = ({ title, to, icon, selected, setSelected }) => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    return (
      <MenuItem 
       
        active={selected === title}
        style={{
          color: colors.grey[100],
        }}
        onClick={() => setSelected(title)}
        icon={icon}
        component={<Link to={to} />}
      >
        <Typography>{title}</Typography>
        
      </MenuItem>
    );
  };
  Item.propTypes = {
    title: PropTypes.string,
    to:PropTypes.string,
    icon : PropTypes.element ,
    selected  : PropTypes.string,
    setSelected   : PropTypes.func,
  }