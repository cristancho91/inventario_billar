import {Typography, Grid,TextField}from '@mui/material';

export const LoginForm=()=>{

    return(
        <Grid container  >
             <Grid item xs={8} md={12} textAlign="center">
                <Typography variant="h1">Login</Typography><br/>
            </Grid>
            
            <Grid container columns={{ xs: 4, md: 12 }} justifyContent="center" alignItems="center">
                <Grid item md={4}>
                    <TextField id='outlined-basic' label='Nombre' variant='filled' />
                </Grid>
                <Grid item md={6}>
                    <TextField id='outlined-basic' label='Email' variant='filled'/>
                </Grid>

            </Grid>

        </Grid>
    )
}