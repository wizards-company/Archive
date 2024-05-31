'use client';
import React from 'react';
import fundo from '../../../public/assets/fundo.jpg'

function MyPage() {
  const css = `
  body{
    font-family: Arial, Helvetica, sans-serif;
    display: flex;
    justify-content: center;
    min-height: 100vh;
    background-image: url(${fundo.src});
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
.box{
    color: white;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    background-color: rgba(0, 0, 0, 0.6);
    padding: 15px;
    border-radius: 15px;
    width: 20%;
}
fieldset{
    border: 3px solid rgb(255, 217, 0);
}
legend{
    border: 1px solid rgb(255, 217, 0);
    padding: 10px;
    text-align: center;
    background-image: linear-gradient(to right,rgb(255, 217, 0), rgb(220, 173, 20));
    border-radius: 8px;
}
.inputBox{
    position: relative;
}
.inputUser{
    background: none;
    border: none;
    border-bottom: 1px solid white;
    outline: none;
    color: white;
    font-size: 15px;
    width: 100%;
    letter-spacing: 2px;
}
.labelInput{
    position: absolute;
    top: 0px;
    left: 0px;
    pointer-events: none;
    transition: .5s;
}
.inputUser:focus ~ .labelInput,
.inputUser:valid ~ .labelInput{
    top: -20px;
    font-size: 12px;
    color: rgb(255, 195, 30);
}
#data_nascimento{
    border: none;
    padding: 8px;
    background-image: linear-gradient(to right,rgb(255, 217, 0), rgb(220, 173, 20));
    border-radius: 10px;
    outline: none;
    font-size: 15px;
}
#submit{
    background-image: linear-gradient(to right,rgb(255, 217, 0), rgb(220, 173, 20));
    width: 100%;
    border: none;
    padding: 15px;
    color: white;
    font-size: 15px;
    cursor: pointer;
    border-radius: 10px;
}
#submit:hover{
    background-image: linear-gradient(to right,rgb(255, 217, 0), rgb(220, 173, 20));
}
  `
  return (
    <main>
      <style>
        {css}
      </style>
      <div className="box">
        <form action="">
          <fieldset>
            <legend><b>CADASTRO BIBLIOTECA</b></legend>
            <br />
            <div className="inputBox">
              <input type="text" name="nome" id="nome" className="inputUser" required />
              <label htmlFor="nome" className="labelInput">Nome Completo</label>
            </div>
            <br /><br />
            <div className="inputBox">
              <input type="text" name="email" id="email" className="inputUser" required />
              <label htmlFor="email" className="labelInput">Email</label>
            </div>
            <br /><br />
            <div className="inputBox">
              <input type="tel" name="telefone" id="telefone" className="inputUser" required />
              <label htmlFor="telefone" className="labelInput">Telefone</label>
            </div>
            <br /><br />
            <div className="inputBox">
              <input type="password" name="password" id="password" className="inputUser" required />
              <label htmlFor="password" className="labelInput">Senha</label>
            </div>
            <br /><br />
            <label htmlFor="data_nascimento"><b>🐻‍❄️ </b></label>
            <input type="date" name="data_nascimento" id="data_nascimento" required />
            <br /><br /><br />
            <input type="submit" name="submit" id="submit" />
          </fieldset>
        </form>
      </div>
    </main>
  );
}
export default MyPage;