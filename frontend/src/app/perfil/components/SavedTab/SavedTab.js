import CardBook from "@/components/CardBook"
import style from "./SavedTab.module.css"

export default function SavedTab({ profileInfo }) {
  return (
    <div className={style.container}>
      {profileInfo[0].saved.map((item, id) => (
        <CardBook key={id} />
      ))}
    </div>
  )
}
