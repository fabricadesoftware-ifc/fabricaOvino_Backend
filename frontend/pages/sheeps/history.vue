<template>
  <section>
    <PageTitle
      icon="sheep"
      :main="$t('pages.pagetitle.sheep_edit.title')"
      :sub="$t('pages.pagetitle.sheep_edit.subtitle')"
    />
    <b-tabs>
      <b-tab-item :label="$t('pages.admin.shearing.tabs.main')">
        <shearing-info v-model="sheep" />
      </b-tab-item>
      <b-tab-item :label="$t('pages.birth.tabs.main')">
        <birth-info />
      </b-tab-item>
    </b-tabs>
  </section>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import BirthInfo from '@/components/sheeps/info/BirthInfo.vue'
import ShearingInfo from '../../components/sheeps/info/ShearingInfo.vue'
export default {
  components: { PageTitle, BirthInfo, ShearingInfo },
  asyncData({ params }) {
    return {
      sheep: params.sheep
    }
  },
  data() {
    return {
      data: {}
    }
  }
}
</script>

<style></style>
