import { Box, useTheme, Typography} from "@mui/material";
import { Header } from "../../components/Header";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore"
import { tokens } from "../../theme";


export const FAQ =()=>{
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);


    return (
        <Box m="20px">
            <Header title="FAQ" subtitle="Frecuently asked questions page" />

            <Accordion defaultExpanded>
                <AccordionSummary expandIcon={<ExpandMoreIcon/>}>
                    <Typography variant="h5" color={colors.greenAccent[500]}>What is the difference between a PWA and an app?</Typography>
                </AccordionSummary>
                <AccordionDetails sx={{bgcolor:colors.background}}>
                    <Typography paragraph>A Progressive Web App or PWA is a web application that uses modern web capabilities to deliver an experience like native </Typography>
                </AccordionDetails>
            </Accordion>
            <Accordion defaultExpanded={false}>
                <AccordionSummary expandIcon={<ExpandMoreIcon/>}>
                    <Typography variant="h5" color={colors.greenAccent[500]}>What is the difference between a PWA and an app?</Typography>
                </AccordionSummary>
                <AccordionDetails sx={{bgcolor:colors.background}}>
                    <Typography paragraph>A Progressive Web App or PWA is a web application that uses modern web capabilities to deliver an experience like native </Typography>
                </AccordionDetails>
            </Accordion>
            <Accordion  defaultExpanded={false}>
                <AccordionSummary expandIcon={<ExpandMoreIcon/>}>
                    <Typography variant="h5" color={colors.greenAccent[500]}>What is the difference between a PWA and an app?</Typography>
                </AccordionSummary>
                <AccordionDetails sx={{bgcolor:colors.background}}>
                    <Typography paragraph>A Progressive Web App or PWA is a web application that uses modern web capabilities to deliver an experience like native </Typography>
                </AccordionDetails>
            </Accordion>
            <Accordion  defaultExpanded={false}>
                <AccordionSummary expandIcon={<ExpandMoreIcon/>}>
                    <Typography variant="h5" color={colors.greenAccent[500]}>What is the difference between a PWA and an app?</Typography>
                </AccordionSummary>
                <AccordionDetails sx={{bgcolor:colors.background}}>
                    <Typography paragraph>Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam ducimus dolores, placeat laborum voluptatibus possimus alias minima in quae vero, quo non tempora, id est blanditiis. Expedita ipsa quia harum.
                    Omnis voluptas quod, nesciunt modi pariatur laborum fugit ad magni officiis doloremque consectetur adipisci ipsa eius inventore, culpa impedit ipsam nobis minus tenetur asperiores alias deleniti at quisquam! Deserunt, hic.
                    Praesentium quibusdam placeat natus soluta rerum sapiente ipsum accusamus earum velit harum! Repellendus itaque odit minus laudantium inventore officia commodi consequuntur porro dolor fuga veritatis aut minima, quod repudiandae alias.
                    Esse dolor numquam mollitia reiciendis nulla officia placeat eligendi. Assumenda esse mollitia, neque possimus, animi sit eaque saepe earum itaque nam necessitatibus nesciunt pariatur voluptatibus adipisci incidunt ipsum ad rerum. </Typography>
                </AccordionDetails>
            </Accordion>
        </Box>
    );
}