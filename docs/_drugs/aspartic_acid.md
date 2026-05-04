---
layout: default
title: Aspartic Acid
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 1
---

# Aspartic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Aspartic Acid：從胺基酸代謝到腎小管酸中毒

## 一句話總結

Aspartic Acid（天冬胺酸）是人體內源性胺基酸，目前在台灣/香港無核准上市藥品許可證，無明確的原核准適應症。
TxGNN 模型預測它可能對**腎小管酸中毒（Renal Tubular Acidosis）** 有潛在相關性，
然而目前**無任何直接臨床試驗**，現有文獻 **10 篇**均為機轉或遺傳研究，不構成直接藥效學證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准適應症（內源性胺基酸） |
| 預測新適應症 | 腎小管酸中毒（Renal Tubular Acidosis） |
| TxGNN 預測分數 | 99.47% |
| 證據等級 | L4（僅有機轉研究與前臨床資料） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，天冬胺酸（Aspartic acid）是人體非必需胺基酸，廣泛參與細胞代謝，其在腎小管酸中毒（RTA）中的機轉關聯性來自以下三條間接路徑：

**路徑一：腎小管能量代謝**。天冬胺酸透過草醯乙酸–天冬胺酸穿梭（malate-aspartate shuttle）參與 NADH 的跨膜轉運，影響腎小管細胞的能量代謝效率。當此路徑受損時，腎小管酸化功能可能隨之下降。

**路徑二：SLC22A13 轉運蛋白介導**。研究（PMID: 24147638）顯示，SLC22A13 位於腎集尿管 A 型間隔細胞基底外側膜，負責天冬胺酸/麩胺酸的單向外流，此轉運蛋白與 AE1（anion exchanger 1，RTA 相關突變位點）共同定位，顯示天冬胺酸代謝與 RTA 病理存在空間上的功能關聯。

**路徑三：代謝性酸中毒下的氮代謝角色**。在代謝性酸中毒狀態下，腎臟氨基生成（ammoniagenesis）顯著增加，天冬胺酸作為氮供體參與尿素循環與 NH₃ 生成（PMID: 14301365, 5641145），間接協助腎臟的酸排泌代償機制。此外，鳥胺酸–天冬胺酸複合製劑（ornithine-aspartate）在一早期酸鹼相關案例中有使用紀錄（PMID: 990372）。

整體而言，機轉推論具一定合理性，但因果鏈條較長且缺乏直接藥效學驗證，屬於假說生成階段。

---

## 臨床試驗證據

> ⚠️ 搜尋結果中僅有 1 個臨床試驗，且與腎小管酸中毒無直接關聯。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04725812](https://clinicaltrials.gov/study/NCT04725812) | Phase 2 | 提前終止 | 2 | 主適應症為子癇前症（Preeclampsia），針對補體調節系統（Eculizumab），與 RTA 無直接關聯；僅招募 2 人即終止，統計效力為零，對本適應症臨床證據貢獻為零 |

**備註**：目前無針對 Aspartic Acid 用於腎小管酸中毒的直接臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [990372](https://pubmed.ncbi.nlm.nih.gov/990372/) | 1976 | 臨床案例系列 | Biomedicine | 鳥胺酸–天冬胺酸靜脈輸注用於含 RTA 的遺傳代謝病童，為天冬胺酸在 RTA 相關情境中最直接的早期臨床紀錄 |
| [24147638](https://pubmed.ncbi.nlm.nih.gov/24147638/) | 2014 | 機轉/轉運蛋白研究 | The Biochemical Journal | SLC22A13 位於 A 型間隔細胞基底外側膜，與 AE1 共定位，介導天冬胺酸/麩胺酸單向外流，直接支持天冬胺酸代謝與 RTA 病灶部位的機轉關聯 |
| [2884989](https://pubmed.ncbi.nlm.nih.gov/2884989/) | 1987 | 動物研究（代謝追蹤） | The Biochemical Journal | 在慢性代謝性酸中毒大鼠腎小管中，麩胺酸（天冬胺酸代謝前驅物）碳骨架代謝途徑發生顯著改變，揭示酸鹼環境對腎小管胺基酸代謝的影響 |
| [5641145](https://pubmed.ncbi.nlm.nih.gov/5641145/) | 1968 | 動物研究 | Nature | 代謝性酸中毒大鼠腎臟代謝中間物濃度改變，包含胺基酸代謝相關路徑 |
| [14301365](https://pubmed.ncbi.nlm.nih.gov/14301365/) | 1965 | 基礎科學 | Am J Physiology | 腎小管細胞氨基生成與 NH₃ 排泌關係研究，天冬胺酸作為氮來源間接參與腎臟酸排泌代償機制 |
| [6422151](https://pubmed.ncbi.nlm.nih.gov/6422151/) | 1983 | 案例報告 | J Inherited Metabolic Disease | 丙酮酸羧化酶缺乏症合併近端 RTA 與胱胺酸尿症病童，補充天冬胺酸後臨床改善，為罕見的直接用藥觀察紀錄 |
| [26208211](https://pubmed.ncbi.nlm.nih.gov/26208211/) | 2015 | 遺傳診斷研究 | Jornal de Pediatria | 以全外顯子定序診斷 4 名遠端 RTA 兒童，闡明 RTA 遺傳病理機制（背景知識） |
| [20068363](https://pubmed.ncbi.nlm.nih.gov/20068363/) | 2010 | 遺傳研究 | Nephron Physiology | 菲律賓兒童 SLC4A1（AE1）基因突變導致遠端 RTA 的遺傳基礎研究 |
| [12087557](https://pubmed.ncbi.nlm.nih.gov/12087557/) | 2002 | 遺傳研究 | Am J Kidney Diseases | AE1 基因 G701D 突變導致體隱性遠端 RTA，說明 AE1 病理機制（背景知識） |
| [23053187](https://pubmed.ncbi.nlm.nih.gov/23053187/) | 2013 | 案例報告 | Annals of Hematology | AE1 A858D 同型合子患者，合併低血鉀性遠端 RTA 與溶血性貧血，記錄 AE1 多效性病理表現 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 目前無台灣/香港上市許可，亦無 DDI、警語或禁忌症相關資料可供評估。在推進任何臨床應用前，須先完成完整的安全性資料蒐集。

---

## 結論與下一步

**決策：Hold**

**理由：**
現有證據僅停留在機轉假說與間接基礎研究層面（L4），缺乏任何針對天冬胺酸用於腎小管酸中毒的直接臨床試驗或對照研究；唯一搜尋到的臨床試驗與本適應症無關且已提前終止。加上藥物本身在台灣/香港無上市許可、MOA 缺失、安全性資料空白，現階段條件尚不足以推進至臨床評估。

**若要推進需要：**
- 補充完整的作用機轉（MOA）資料，從 DrugBank API 查詢 DB00128 詳細資訊
- 確認是否存在針對天冬胺酸或鳥胺酸–天冬胺酸複合製劑（ornithine-aspartate）用於 RTA 的專屬臨床研究或個案系列
- 完成 TFDA/衛福部仿單警語、禁忌症資料蒐集（現為 Blocking Data Gap）
- 評估給藥途徑可行性（目前 available routes 未記錄）
- 進行前臨床（In vitro/In vivo）藥效學驗證以強化機轉連結，達到 L3 前不建議進入臨床規劃
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

