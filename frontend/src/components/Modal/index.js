import Link from "next/link";
import style from "./modal.module.css"


export default function Modal({ isModalClosed, setIsModalClosed }) {
    const toggleModal = isModalClosed ? style.hidden : null
    function closeModal() {
        setIsModalClosed(prev => !prev)
    }

    return (
        <nav className={`${style.modal} ${toggleModal}`}>
            <div onClick={() => closeModal()} className={style.x}>
                <div className={`${style.line} ${style.lineA}`}></div>
                <div className={`${style.line} ${style.lineB}`}></div>
            </div>
            <ul className={style.list}>
                <li><Link href="/contanto">Livros</Link></li>
                <li><Link href="/">Salvos</Link></li>
            </ul>
        </nav>
    )
}