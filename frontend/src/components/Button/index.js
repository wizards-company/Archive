import Link from "next/link";
import style from "./button.module.css"

export default function Button({ text = "texto", href = "/" }) {

    // Faz a primeira letra do text maiúscula 
    const newText = text.slice(0, 1).toUpperCase().concat(text.slice(1))

    return (
        <Link className={style.container} href={href}>
            <p className={style.btn}>{newText}</p>
        </Link>
    )
}