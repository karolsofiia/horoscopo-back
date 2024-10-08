const express = require('express');
const {urlencoded, json} = require('express');
const router = require('./routes/signos.routes.js');
const cors = require('cors');

const app = express();

app.use(urlencoded({extended: true}))
app.use(json())
app.get('/', async (req,res) => {
    res.send("Hola soy el back del horoscopo de karlakarolynico");
});
app.use(cors())
app.use('/v1/signos', router);

app.listen(4000, ()=>{
    console.log('listening at port 4000');
})