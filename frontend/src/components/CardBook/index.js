import Button from '../Button';
import ProfileIcon from '../ProfileIcon';
import style from './card.module.css';
import saved from "/src/assets/saved.png"
import message from "/src/assets/message.png"
import Container from '../Container';
export default function CardBook() {
    const books = [1, 2, 3, 4, 5, 6, 7, 8]
    return (
        <Container>
            <div className={style.container}>
                {books.map((item, id) => (
                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon />
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <Button p="0" width={14} variant="green" icon={saved} />
                            <Button p="0" width={15} variant="green" icon={message} />
                            <Button text="pedir" p="1px 14px" variant="blue" textColor="--base-white" />
                        </div>
                    </div>
                ))}
                <div className={style.div}>
                    <Button text="Ver todos os livros" variant="blue" textColor="--base-white" />
                </div>
            </div>
        </Container>
    )
}