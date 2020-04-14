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
  <!-- <aside class="column is-2 section">
    <p class="menu-label is-hidden-touch"></p>
    <ul class="menu-list">
      <li v-for="(item, key) of items" :key="key">
        <nuxt-link :to="localePath(item.to)" exact-active-class="is-info">
          <b-icon :icon="item.icon" /> {{ item.title }}
        </nuxt-link>
      </li>
    </ul>
    <p class="menu-label is-hidden-touch">
      {{ $t("asideMenu.adminItems.title") }}
    </p>
    <ul class="menu-list">
      <li v-for="(item, key) of adminItems" :key="key">
        <nuxt-link :to="localePath(item.to)" exact-active-class="is-info">
          <b-icon :icon="item.icon" /> {{ item.title }}
        </nuxt-link>
      </li>
    </ul>
  </aside>-->
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
        {
          title: "Inspire",
          icon: "lightbulb",
          to: { name: "inspire" },
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
