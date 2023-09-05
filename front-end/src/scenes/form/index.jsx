import { Box, Button, TextField } from "@mui/material";
import {Formik} from "formik";
import * as yup from 'yup';
import useMediaQuery from "@mui/material/useMediaQuery";
import { Header } from "../../components/Header";

export const Form = () =>{
    const isNonMobile = useMediaQuery('(min-width: 600px)');

    const handleFormSubmit = (values)=>{
        console.log(values);
    }

    return (
        <Box m="20px" >
            <Header title="CREATE USER" subtitle="Create a New Profile User" />

            <Formik 
            onSubmit={handleFormSubmit}
            initialValues={initialValues}
            validationSchema= {checkoutSchema}
            >
                {({
                    
                    values,
                    errors,
                    touched,
                    handleBlur,
                    handleChange,
                    handleSubmit
                    }) => (
                        <form onSubmit={handleSubmit}>
                            {/* first Name */}
                            <Box 
                            display="grid"
                            gap="30px"
                            gridTemplateColumns="repeat(4, minmax(0,1fr))"
                            sx={{
                                "& > div":{
                                    gridColumn: isNonMobile ? undefined : "span 4"
                                },
                            }}
                            > 
                                <TextField 
                                    fullWidth
                                    variant="filled"
                                    type="text"
                                    label="firs name"
                                    onBlur={handleBlur}
                                    onChange={handleChange}
                                    value={values.firsName}
                                    name="firsName"
                                    error={!!touched.firsName && !!errors.firsName}
                                    helperText={touched.firsName && errors.firsName}
                                    sx={{
                                        gridColumn: "span 2"
                                    }}
                                />
                                <TextField 
                                    fullWidth
                                    variant="filled"
                                    type="text"
                                    label="Last Name"
                                    onBlur={handleBlur}
                                    onChange={handleChange}
                                    value={values.lastName}
                                    name="lastName"
                                    error={!!touched.lastName && !!errors.lastName}
                                    helperText={touched.lastName && errors.lastName}
                                    sx={{
                                        gridColumn: "span 2"
                                    }}

                                />

                                <TextField 
                                    fullWidth
                                    variant="filled"
                                    type="text"
                                    label="Email"
                                    onBlur={handleBlur}
                                    onChange={handleChange}
                                    value={values.email}
                                    name="email"
                                    error={!!touched.email && !!errors.email}
                                    helperText={touched.email && errors.email}
                                    sx={{
                                        gridColumn :"span 4"
                                    }}
                                
                                />

                                <TextField 
                                    fullWidth
                                    variant="filled"
                                    type="text"
                                    label="Contact Numbuer"
                                    onBlur={handleBlur}
                                    onChange={handleChange}
                                    value={values.contact}
                                    name="contact"
                                    error={!!touched.contact && !!errors.contact}
                                    helperText={touched.contact && errors.contact}
                                    sx={{
                                        gridColumn: "span 4"
                                    }}
                                />
                                 <TextField
                                    fullWidth
                                    variant="filled"
                                    type="text"
                                    label="Address 1"
                                    onBlur={handleBlur}
                                    onChange={handleChange}
                                    value={values.address1}
                                    name="address1"
                                    error={!!touched.address1 && !!errors.address1}
                                    helperText={touched.address1 && errors.address1}
                                    sx={{ gridColumn: "span 4" }}
                                />
                                <TextField
                                    fullWidth
                                    variant="filled"
                                    type="text"
                                    label="Address 2"
                                    onBlur={handleBlur}
                                    onChange={handleChange}
                                    value={values.address2}
                                    name="address2"
                                    error={!!touched.address2 && !!errors.address2}
                                    helperText={touched.address2 && errors.address2}
                                    sx={{ gridColumn: "span 4" }}
                                />
                            </Box>

                            <Box display="flex" justifyContent="end" mt="20px">
                                <Button type="submit" color="secondary" variant="contained">
                                    Create New User
                                </Button>
                            </Box>
                        </form>
                    )}
                
            </Formik>

        </Box>
    )
    
}

const phoneRegExp = /^((\+[1-9]{1,4}[ -]?)|(\([0-9]{2,3}\)[ -]?)|([0-9]{2,4})[ -]?)*?[0-9]{3,4}[ -]?[0-9]{3,4}$/;

const checkoutSchema  = yup.object().shape({
    firsName: yup.string().required("Este campo es requerido"),
    lastName: yup.string().required("este campo es requerido"),
    email: yup.string().email("invalid email").required("email requerido"),
    contact : yup
        .string()
        .matches(phoneRegExp, "el numero telefonico no es valido")
        .required("este campo es requerido"),
        address1: yup.string().required("este campo es requerido"),
        address2: yup.string().required("este campo es requerido"),
})

const initialValues = {
    firsName: "",
    lastName:"",
    contact :"",
    email: "",
    address1: "",
    address2: "" ,
}