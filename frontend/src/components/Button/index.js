"use client"
import Link from "next/link";
import style from "./button.module.css"
import Image from "next/image";

export default function Button({ text = undefined, href = "/", variant, icon = undefined, weight, p = "5px 10px", textColor = "--base-black", width }) {
    // Faz a primeira letra do text maiúscula 
    const newText = text ? text.slice(0, 1).toUpperCase().concat(text.slice(1)) : null
    const classVariant = style[variant]

    const divProps = {
        padding: p,
    }
    const pProps = {
        fontWeight: weight,
        color: `var(${textColor})`
    }

    const iconProps = {
        width: width
    }

    return (
        <Link className={style.container} href={href}>
            <div style={divProps} className={`${style.btn} ${classVariant}`}>
                {newText && <p style={pProps} className={`${style.text}`}>{newText}</p>}
                {icon &&
                    <div className={`${style.icon}`}>
                        <Image style={iconProps} className={style.iconImg}
                            src={icon} />
                    </div>
                }
            </div>
        </Link>
    )
}