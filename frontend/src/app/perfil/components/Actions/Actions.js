import style from "./Actions.module.css"
import add from "@/assets/add.png"
import edit from "@/assets/edit.png"
import logout from "@/assets/logout.png"
import Button from "@/components/Button";

export default function Actions() {
  return (
    <div className={style.actionsContainer}>
      <div className={style.actions}>
        <div className={style.perfil}></div>
        <div className={style.actionsButtonsContainer}>
          <div>Nome do usuário</div>
          <div className={style.actionsButtons}>
            <Button href="" icon={logout} width={"15px"} variant={"red"} p="0px" text={"sair"} fontSize={"14px"} weight={300} textColor="--base-white" />
            <Button href="/editarPerfil" icon={edit} width={"15px"} variant={"green"} p="0px" fontSize={"14px"} weight={300} text={"Editar perfil"} textColor="--base-white" />
            <Button href="/adicionarLivro" icon={add} width={"15px"} variant={"blue"} p="0px" fontSize={"14px"} weight={300} text={"Adicionar livro"} textColor="--base-white" />
          </div>
        </div>
      </div>
    </div>
  )
}