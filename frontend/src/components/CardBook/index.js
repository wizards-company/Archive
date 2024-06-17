import Button from '../Button';
import ProfileIcon from '../ProfileIcon';
import style from './card.module.css';

export default function CardBook() {

    return (
        <section className={style.container}>
            <div className={style.card}>
                <div className={style.containerMenor}>
                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon/>
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <img className={style.icon} src="#" alt="icon" />
                            <img className={style.icon} src="#" alt="icon" />
                            <Button text="Pedir" variant="blue" e textColor="--base-white"/>
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon/>
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <img className={style.icon} src="#" alt="icon" />
                            <img className={style.icon} src="#" alt="icon" />
                            <Button text="Pedir" variant="blue" e textColor="--base-white"/>
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon/>
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <img className={style.icon} src="#" alt="icon" />
                            <img className={style.icon} src="#" alt="icon" />
                            <Button text="Pedir" variant="blue" e textColor="--base-white"/>
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon/>
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <img className={style.icon} src="#" alt="icon" />
                            <img className={style.icon} src="#" alt="icon" />
                            <Button text="Pedir" variant="blue" e textColor="--base-white"/>
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon/>
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <img className={style.icon} src="#" alt="icon" />
                            <img className={style.icon} src="#" alt="icon" />
                            <Button text="Pedir" variant="blue" e textColor="--base-white"/>
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon/>
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <img className={style.icon} src="#" alt="icon" />
                            <img className={style.icon} src="#" alt="icon" />
                            <Button text="Pedir" variant="blue" e textColor="--base-white"/>
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon/>
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <img className={style.icon} src="#" alt="icon" />
                            <img className={style.icon} src="#" alt="icon" />
                            <Button text="Pedir" variant="blue" e textColor="--base-white"/>
                            
                        </div>
                    </div>

                    <div className={style.cardBook}>
                        <div className={style.titulos}>
                            <ProfileIcon/>
                            <h3 className={style.autor}>Nome do autor</h3>
                        </div>
                        <img className={style.book} src="#" alt="icon" />
                        <div className={style.infos}>
                            <img className={style.icon} src="#" alt="icon" />
                            <img className={style.icon} src="#" alt="icon" />
                            <Button text="Pedir" variant="blue" e textColor="--base-white"/>
                        </div>
                    </div>

                    <div className={style.div}>
                    <Button text="Ver todos os livros" variant="blue" e textColor="--base-white"/>
                    </div>


                    </div>
            </div>
        </section>
    )
}