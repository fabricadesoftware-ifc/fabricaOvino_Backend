<template>
  <section>
    <PageTitle
      icon="sheep"
      :main="$t('pages.pagetitle.sheep_edit.title')"
      :sub="$t('pages.pagetitle.sheep_edit.subtitle')"
    />
    <b-tabs>
      <b-tab-item :label="$t('pages.sheeps.edit.generalInfo')">
        <general-info v-model="sheep" />
      </b-tab-item>
      <b-tab-item :label="$t('pages.birth.tabs.main')"> </b-tab-item>
    </b-tabs>
  </section>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import GeneralInfo from '@/components/sheeps/GeneralInfo'
export default {
  asyncData({ params }) {
    return {
      sheep: params.sheep
    }
  },
  data() {
    return {
      data: {}
    }
  },
  components: { GeneralInfo, PageTitle }
}
</script>

<style></style>
