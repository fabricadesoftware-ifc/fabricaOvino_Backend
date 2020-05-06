<template>
  <aside class="tile is-child menu">
    <b-menu>
      <b-menu-list :label="$t('asideMenu.general')">
        <b-menu-item
          v-for="(item, key) of items"
          :key="key"
          tag="nuxt-link"
          :to="localePath(item.to)"
          :icon="item.icon"
          :label="item.title"
        ></b-menu-item>
      </b-menu-list>
      <b-menu-list :label="$t('asideMenu.adminItems.title')">
        <b-menu-item
          v-for="(item, key) of adminItems"
          :key="key"
          tag="nuxt-link"
          :to="localePath(item.to)"
          :icon="item.icon"
          :label="item.title"
        ></b-menu-item>
      </b-menu-list>
    </b-menu>
  </aside>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          title: "Home",
          icon: "home",
          to: { name: "index" },
        },
      ],
      adminItems: [
        {
          title: this.$t("asideMenu.adminItems.category"),
          icon: "alpha-c-circle-outline",
          to: { name: "admin-category" },
        },
        {
          title: this.$t("asideMenu.adminItems.breed"),
          icon: "puzzle",
          to: { name: "admin-breed" },
        },
        {
          title: this.$t("asideMenu.adminItems.sheep"),
          icon: "sheep",
          to: { name: "admin-sheep" },
        },
        {
          title: this.$t("asideMenu.adminItems.pregnancyDiagnosis"),
          icon: "human-pregnant",
          to: { name: "admin-pregnancyDiagnosis" },
        },
        {
          title: this.$t("asideMenu.adminItems.birth"),
          icon: "lightbulb-outline",
          to: { name: "birth" },
        },
      ],
    };
  },
};
</script>

<style>
.menu {
  margin-left: 10px;
  border-radius: 12px;
  background-color: azure;
  font-size: 1.1rem;
}
</style>
