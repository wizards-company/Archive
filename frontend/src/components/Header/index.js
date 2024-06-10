"use client"
import style from "./header.module.css";
import Link from "next/link";
import ProfileIcon from "../ProfileIcon";
import { useState } from "react";
import Button from "../Button";

export default function Header() {
  const [isLogged, setIsLogged] = useState(true)
  return (
    <header className={style.container}>
      <Link href="/" className={style.logo}>Libs</Link>
      {isLogged ?
        <nav className={style.nav}>
          <Link className={style.navItem} href="Livros">
            Livros
          </Link>
          <Link className={style.navItem} href="Salvos">
            Salvos
          </Link>
          <Link className={style.navItem} href="Blogs">
            Blogs
          </Link>
          <div className={style.icon}>
            <ProfileIcon />
          </div>
        </nav>
        :
        <nav className={style.nav}>
          <Link className={style.navItem} href="Blogs">
            Blogs
          </Link>
          <Button text="Registrar" href="/registrar" />
          <Button text="Logar" href="/login" />
        </nav>
      }
    </header>
  );
}
