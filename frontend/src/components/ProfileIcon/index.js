import Link from "next/link"
import style from "./profileIcon.module.css"

export default function ProfileIcon() {
  return (
    <Link style={{ height: "28px" }} href="/perfil">
      <svg
        className={style.svg}
        width="29"
        height="29"
        viewBox="0 0 29 29"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <rect
          className={style.icon}
          x="0.5"
          y="0.5"
          width="27.52"
          height="27.52"
          fill="#FF964A"
          stroke="black"
        />
        <path
          d="M23.84 20.72C23.84 22.7745 19.3987 24.44 13.92 24.44C8.44134 24.44 4 22.7745 4 20.72C4 18.6655 8.44134 17 13.92 17C19.3987 17 23.84 18.6655 23.84 20.72Z"
          fill="black"
        />
        <circle cx="14" cy="9" r="5" fill="black" />
      </svg>
    </Link>
  )
}
