<template>
  <div id="content">
    <p class="title" id="tit">Ogłoszenia</p>

    <div id="announcements">
      <announcement
        :author="annAuthor"
        :category="annCategory"
        :date="annDate"
        :title="annTitle"
        :content="annContent"
        />

      <announcement
        :author="annAuthor"
        :category="annCategory"
        :date="annDate"
        :title="annTitle"
        :content="annContent"/>

      <announcement
        :author="annAuthor"
        :category="annCategory"
        :date="annDate"
        :title="annTitle"
        :content="annContent"/>

      <announcement
        :author="annAuthor"
        :category="annCategory"
        :date="annDate"
        :title="annTitle"
        :content="annContent"/>

      <announcement
        :author="annAuthor"
        :category="annCategory"
        :date="annDate"
        :title="annTitle"
        :content="annContent"/>

      <announcement
        :author="annAuthor"
        :category="annCategory"
        :date="annDate"
        :title="annTitle"
        :content="annContent"/>

      <announcement
        :author="annAuthor"
        :category="annCategory"
        :date="annDate"
        :title="annTitle"
        :content="annContent"/>

      <announcement
        :author="annAuthor"
        :category="annCategory"
        :date="annDate"
        :title="annTitle"
        :content="annContent"/>
    </div>
  </div>
</template>

<script>
import announcement from "./announcement.vue";

export default {
  name: "announcements",
  components: {
    announcement,
  }, 
  data() {
    return {
      annAuthor: 'Jan Kowalski',
      annCategory: 'Poszukiwanie sponsora',
      annDate: '12.08.2022r. 17:20',
      annTitle: 'Poszukiwany inwestor',
      annContent: 'Treść Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci sit, dolor rerum repudiandae accusamus porro ea cum! Corrupti laboriosam facere debitis libero deserunt minus at, iure consequuntur eaque nesciunt nostrum exercitationem praesentium, molestias aliquam perferendis rem enim porro illum recusandae possimus nobis inventore. Treść Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci sit, dolor rerum repudiandae accusamus porro ea cum! Corrupti laboriosam facere debitis libero deserunt minus at, iure consequuntur eaque nesciunt nostrum exercitationem praesentium, molestias aliquam perferendis rem enim porro illum recusandae possimus nobis inventore.', 
    }
  }
};
</script>

<style>
.title {
  padding: 10px;
  font-size: 40px;
}

#tit {
  text-align: left;
}

#announcements {
  width: 100%;
  height: 90%;
  background-color: white;
  overflow: auto;
}

</style>