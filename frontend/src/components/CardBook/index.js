import Button from '../Button';
import ProfileIcon from '../ProfileIcon';
import style from './card.module.css';
import saved from "/src/assets/saved.png"
import message from "/src/assets/message.png"
export default function CardBook() {

    return (
        <section className={style.container}>
            <div className={style.card}>
                <div className={style.containerMenor}>
                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon />
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <Button p={2} width={17} variant="green" icon={saved} />
                            <Button p={2} width={20} variant="green" icon={message} />
                            <Button text="Pedir" variant="blue" e textColor="--base-white" />
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon />
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <Button p={2} width={17} variant="green" icon={saved} />
                            <Button p={2} width={20} variant="green" icon={message} />
                            <Button text="Pedir" variant="blue" e textColor="--base-white" />
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon />
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <Button p={2} width={17} variant="green" icon={saved} />
                            <Button p={2} width={20} variant="green" icon={message} />
                            <Button text="Pedir" variant="blue" e textColor="--base-white" />
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon />
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <Button p={2} width={17} variant="green" icon={saved} />
                            <Button p={2} width={20} variant="green" icon={message} />
                            <Button text="Pedir" variant="blue" e textColor="--base-white" />
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon />
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <Button p={2} width={17} variant="green" icon={saved} />
                            <Button p={2} width={20} variant="green" icon={message} />
                            <Button text="Pedir" variant="blue" e textColor="--base-white" />
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon />
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <Button p={2} width={17} variant="green" icon={saved} />
                            <Button p={2} width={20} variant="green" icon={message} />
                            <Button text="Pedir" variant="blue" e textColor="--base-white" />
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon />
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <Button p={2} width={17} variant="green" icon={saved} />
                            <Button p={2} width={20} variant="green" icon={message} />
                            <Button text="Pedir" variant="blue" e textColor="--base-white" />

                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon />
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <Button p={2} width={17} variant="green" icon={saved} />
                            <Button p={2} width={20} variant="green" icon={message} />
                            <Button text="Pedir" variant="blue" e textColor="--base-white" />
                        </div>
                    </div>

                    <div className={style.div}>
                        <Button text="Ver todos os livros" variant="blue" e textColor="--base-white" />
                    </div>

                </div>
            </div>
        </section>
    )
}