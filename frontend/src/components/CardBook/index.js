import ProfileIcon from "../ProfileIcon/index"
import saved from "@/assets/saved.png"
import message from "@/assets/message.png"
import style from "./CardBook.module.css"
import Button from "../Button"
export default function CardBook() {
  return (
    <div className={style.cardBook}>
      <div className={style.titulos}>
        <ProfileIcon />
        <h3 className={style.autor}>Nome do autor</h3>
      </div>
      <img className={style.book} src="#" alt="icon" />
      <div className={style.infos}>
        <Button p="0" width={14} variant="green" icon={saved} />
        <Button p="0" width={15} variant="green" icon={message} />
        <Button
          text="pedir"
          p="1px 14px"
          variant="blue"
          textColor="--base-white"
        />
      </div>
    </div>
  )
}
