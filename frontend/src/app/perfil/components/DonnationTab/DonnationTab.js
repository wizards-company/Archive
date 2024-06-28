import CardBook from "@/components/CardBook"
import style from "./DonnationTab.module.css"

export default function DonnationTab({ profileInfo }) {
  return (
    <div className={style.container}>
      {profileInfo[0].saved.map((item, id) => (
        <CardBook key={id} />
      ))}
    </div>
  )
}
