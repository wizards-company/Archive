
import Container from "@/components/Container";
import style from "./Perfil.module.css"
import Actions from "./components/Actions/Actions";
import ButtonsContainer from "./components/ButtonsContainer/ButtonsContainer";

export default function Perfil() {
  return (
    <Container>
      <div className={style.flexReverse}>
        <Actions />
        <div className={style.contentContainer}>
          <p className={style.username}>Nome de usuário</p>
          <ButtonsContainer />
        </div>
      </div>
      <div></div>
    </Container>
  )
}