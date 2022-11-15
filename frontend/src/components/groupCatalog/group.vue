<template>
    <div class="container">
        <h1 class="title">Koło naukowe X</h1>
        <p class="p-category">Informatyka</p>
        <br>
        <div class="columns">
          <div class="column is-3">
            <!-- <b-button type="is-light">Forum</b-button>
            <br>
            <b-button type="is-light">O nas</b-button>
            <b-button type="is-light">Czym się zajmujemy</b-button>
            <b-button type="is-light">Członkowie</b-button>
            <b-button type="is-light">Kontakt</b-button>
            <b-button type="is-light">Materiały dydaktyczne</b-button>
            <b-button type="is-light">Projekt dla Ciebie</b-button> -->
            <button type="button" class="button" id="btn">Forum</button>
            <br>
            <button type="button" class="button" id="btn">O nas</button>
            <button type="button" class="button" id="btn">Czym się zajmujemy</button>
            <button type="button" class="button" id="btn">Członkowie</button>
            <button type="button" class="button" id="btn">Kontakt</button>
            <button type="button" class="button" id="btn">Materiały dydaktyczne</button>
            <button type="button" class="button" id="btn">Projekt dla Ciebie</button>
            <!-- <button type="button" class="button is-medium" id="btn">Projekt dla Ciebie</button> -->
          </div>
          <div class="column is-7">Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis quos omnis incidunt asperiores veritatis dolore, nemo accusamus! Distinctio iusto debitis nostrum asperiores aspernatur amet hic dignissimos, atque aliquam earum velit natus incidunt, magni ratione rerum suscipit illo minus commodi? Cupiditate aspernatur minus error at dignissimos id debitis, dolore corporis inventore ipsa! Eveniet, voluptatibus perspiciatis modi officiis quasi autem facere vitae? Facere totam eaque praesentium magni quod impedit esse laborum? Omnis numquam dolores repudiandae quis eius ullam dolore voluptatibus amet saepe suscipit obcaecati, ipsam molestias illo dicta incidunt. Dolor assumenda, sed quas tempora maxime quo blanditiis consequatur? Suscipit temporibus, optio voluptates officia deserunt id minus repudiandae voluptate eveniet qui ut quaerat ex maxime? Tempora dignissimos excepturi consequatur maiores est hic recusandae, nihil et laudantium ipsam dolores vitae ad sed ex deserunt voluptate quod eligendi quibusdam rem molestias adipisci modi architecto. Eaque voluptatem omnis exercitationem consequatur recusandae ab quas voluptates dolore! Voluptatum, tempora quis laborum cumque atque officia eveniet ex sunt praesentium cupiditate, molestiae magni quo. Inventore, nam doloribus labore praesentium accusantium molestias nostrum sapiente, cum ipsum, fugiat recusandae nobis sequi. Vel laboriosam asperiores unde deleniti accusantium nihil at animi, neque assumenda ab, tenetur dolor odit magni amet sunt! Saepe, repellat excepturi!</div>
          <div class="column">
            <div>
              <p class="p-links">Linki</p>
              <a href="https://github.com" target="_blank">Github</a> 
              <a href="https://facebook.com" target="_blank">Facebook</a>
              <a href="https://discord.com" target="_blank">Discord</a>
            </div> 
            <div>
              <br>
              <p class="p-links">Dyski</p>
              <a href="https://drive.google.com/drive/folders/1QMHnaSuOPcfOX16190I9D8q_Fa5pzeOF?usp=sharing" target="_blank">Dysk1</a> 
              <a href="https://drive.google.com/drive/folders/1vGf8f0nVkJcAZQ6S7mZ74vFhpJK0Gbeo?usp=sharing" target="_blank">Dysk2</a>
            </div>
            <!-- <b-menu :activable="false" :accordion="false">
              <b-menu-list label="Szuflada">
                <b-menu-item label="Linki">
                  <b-menu-item label="Link 1"></b-menu-item>
                  <b-menu-item label="Link 2"></b-menu-item>
                </b-menu-item>
                <b-menu-item label="Dyski">
                  <b-menu-item label="Dysk 1"></b-menu-item>
                  <b-menu-item label="Dysk 2"></b-menu-item>
                </b-menu-item>
              </b-menu-list>
            </b-menu> -->
          </div>
        </div>
    </div>
</template>

<script>
export default {
  name: "group",
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.container {
  margin: 0 auto;
}

.title {
  text-align: center;
}

.p-category {
  text-align: center;
  font-size: 16px;
  color: grey;
}

.p-links {
  font-size: 18px;
  color: #7a7a7a;
}

a {
  display: block;
  position: relative;
  padding: 0.5rem 0.75rem;
  line-height: 1.5;
  color: #4a4a4a;
  border: none;
  transition: .3s;
  cursor: pointer;
}

a:hover {
  background-color: #c2baba;
}

#btn {
  margin-bottom: 8px;
  width: 270px;
  justify-content: left;
  color: black;
  background-color: rgb(165, 232, 163);
}

</style>