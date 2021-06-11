const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Full stack python,Avinash nandakumar,avinash.nkbio@gmail.com!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})