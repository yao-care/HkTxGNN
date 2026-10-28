---
layout: default
title: Estradiol Valerate
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Estradiol Valerate：預測新適應症為脆性 X 症候群女性帶因者的症狀性表現 (symptomatic form of fragile X syndrome in female…（證據等級 L5）。原適應症：原發性卵巢衰竭 (primary ovarian failure)"
monitor_inn: "ESTRADIOL VALERATE"
predicted_indications: ["symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 12", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "anovulation", "ovarian remnant syndrome", "luteoma of pregnancy", "ovarian dysfunction"]
---

# Estradiol Valerate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Estradiol Valerate：脆性 X 症候群女性帶因者的症狀性表現
{: .text-alpha }

## 一句話總結

Estradiol Valerate（戊酸雌二醇）是雌激素製劑，原本用於原發性卵巢衰竭（primary ovarian failure）的雌激素補充。
TxGNN 模型預測它可能對**脆性 X 症候群女性帶因者的症狀性表現 (symptomatic form of fragile X syndrome in female carrier)** 有效，但目前**沒有臨床試驗與文獻**直接支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 原發性卵巢衰竭 (primary ovarian failure) |
| 預測新適應症 | 脆性 X 症候群女性帶因者的症狀性表現 (symptomatic form of fragile X syndrome in female carrier) |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，戊酸雌二醇是雌二醇的酯類前驅藥，用於雌激素缺乏狀態的替代療法，其在原發性卵巢衰竭中的角色已被確立，機轉上可能適用於因卵巢功能不足而出現雌激素缺乏的相關族群。

FMR1 前突變的女性帶因者可能發生 FXPOI（脆性 X 相關原發性卵巢功能不全），與原適應症「原發性卵巢衰竭」有重疊。因此，雌激素補充在機轉上具合理性。但這僅針對卵巢功能不足所致的低雌激素狀態，並不代表能改善脆性 X 症候群的其他症狀（如神經認知表現）。

這個連結目前僅為模型預測，沒有任何臨床試驗或文獻佐證。

### 其他預測適應症的簡要觀察

TxGNN 的其他高分預測多數缺乏實質證據：
- **眼瞼狹小-倒轉型內眥贅皮-上瞼下垂症候群（BPES）及其 3q23 重組型**：伴隨卵巢功能不全時，雌激素補充僅可處理卵巢部分，無法處理眼瞼與顱顏特徵。
- **染色體 5p、12p、18p 部分三體/四體**：無明確機轉連結，分數來自 TxGNN 模型（深度學習），可能只是反映模型學到的相關疾病之間的相似性，並非生物學證據。
- **卵巢殘餘症候群、妊娠黃體瘤**：缺乏合理的治療依據，且外源性雌激素可能適得其反或有安全疑慮。
- **無排卵 (anovulation)**：有 1 個 Phase 4 試驗與文獻，但文獻多為動物研究，見下方說明。
- **卵巢功能障礙 (ovarian dysfunction)**：文獻多為動物模型，僅有間接臨床支持。

---

## 臨床試驗證據

針對首位預測適應症（脆性 X 症候群女性帶因者），目前無相關臨床試驗登記。

作為參考，排名第 8 的預測適應症「無排卵」有 1 項相關試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02186782](https://clinicaltrials.gov/study/NCT02186782) | Phase 4 | 未知 | 600 | 比較 clomiphene 併用雌二醇與單用 clomiphene 於不孕女性誘導排卵的效果；尚無結果，無法確認療效 |

---

## 文獻證據

針對首位預測適應症，目前無相關文獻。

作為參考，排名第 10 的「卵巢功能障礙」與第 8 的「無排卵」下，與人體較相關的文獻如下（其餘多為以戊酸雌二醇**誘發**多囊卵巢的動物模型研究，這說明藥物可作為疾病誘發劑，並非治療效果的證據）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36063826](https://pubmed.ncbi.nlm.nih.gov/36063826/) | 2022 | 臨床研究（設計未確認） | Gynecol Endocrinol | 比較不同劑量雌激素對不明原因反覆流產患者子宮內膜雌激素受體表現與卵巢功能的影響 |
| [33749482](https://pubmed.ncbi.nlm.nih.gov/33749482/) | 2021 | 臨床研究（設計未確認） | Gynecol Endocrinol | 戊酸雌二醇/nomegestrol acetate 複方用於卵巢子宮內膜異位瘤與深部浸潤性子宮內膜異位症；屬不同配方，僅間接支持 |
| [40774400](https://pubmed.ncbi.nlm.nih.gov/40774400/) | 2025 | Review | J Steroid Biochem Mol Biol | 回顧 PCOS 動物模型的誘發劑，包含戊酸雌二醇 |
| [1472813](https://pubmed.ncbi.nlm.nih.gov/1472813/) | 1992 | 臨床報告 | J Assist Reprod Genet | 卵子捐贈計畫中以口服戊酸雌二醇 6 mg/日加黃體素作為荷爾蒙替代，用於卵巢衰竭不孕女性 |
| [12960066](https://pubmed.ncbi.nlm.nih.gov/12960066/) | 2003 | 動物研究 | Endocrinology | 青春期前給予戊酸雌二醇使大鼠成年後週期紊亂並出現囊性卵巢 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-48266 | ESTRADE TAB 2MG | 未載明 | 未載明 |
| HK-59784 | QLAIRA TAB | 未載明 | 未載明 |

兩張許可證皆為單一成分製劑、狀態有效。

---

## 安全性考量

以下為知識圖譜中與本藥相關的禁忌疾病關聯（非仿單內容，僅供參考），包含：

- **心血管與代謝**：高血壓、鬱血性心衰竭、糖尿病（含酮酸中毒）、高三酸甘油脂血症、高鈣血症（含惡性腫瘤體液性高鈣血症）
- **肝腎與膽道**：肝臟疾病、腎臟疾病、膽囊疾病
- **內分泌與免疫**：甲狀腺功能低下（含黏液水腫、先天性甲低）、系統性紅斑狼瘡
- **神經精神**：癲癇、焦慮症、精神官能症、輕鬱症
- **其他**：紫質症、氣喘、良性攝護腺增生、男性女乳症、乳房肥大

另外，動物研究提示戊酸雌二醇可能誘發多囊卵巢與無排卵，對排卵功能構成潛在安全訊號。妊娠期間的雌激素暴露亦有安全疑慮。

仿單警語與禁忌的詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測適應症僅有模型分數（0.9994），沒有任何臨床試驗或文獻佐證，證據等級為 L5。機轉上雖與 FXPOI 的雌激素缺乏相關，但僅能處理卵巢部分，無法涵蓋脆性 X 症候群的其他症狀。
- 其他高分預測多缺乏合理機轉或以動物誘發模型為主，不構成療效證據。

**若要推進需要：**
- 補充戊酸雌二醇的作用機轉資料（MOA）
- 取得香港衛生署許可證的核准適應症與仿單警語、禁忌
- 針對 FMR1 前突變女性帶因者／FXPOI 的文獻回顧，並確認是否已有雌激素補充的臨床研究
- 釐清預測適應症究竟指向「卵巢功能不全」還是脆性 X 的其他症狀，以界定目標族群與療效指標
- 評估禁忌疾病族群的安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

