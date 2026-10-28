---
layout: default
title: Progesterone
parent: 高證據等級 (L1-L2)
nav_order: 737
evidence_level: L2
indication_count: 7
monitor_inn: "PROGESTERONE"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "benign mammary dysplasia", "renal hypoplasia, bilateral", "renal hypoplasia (disease)", "apocrine adenosis of breast", "blunt duct adenosis of breast"]
last_modified_at: 2026-10-23
description: "Progesterone：預測新適應症為閉經 (Amenorrhea)（證據等級 L2）。原適應症：知識圖譜記錄的關聯：子宮內膜異位症、子宮內膜癌、停經後骨質疏鬆"
---

# Progesterone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **7** 個
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

## Progesterone：閉經 (Amenorrhea)
{: .text-alpha }

## 一句話總結

Progesterone（黃體素）是天然的女性性腺類固醇荷爾蒙，知識圖譜中記錄的相關用途包括子宮內膜異位症、子宮內膜癌與停經後骨質疏鬆等。
TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 有效，
目前有 **4 個臨床試驗**和 **18 篇文獻**與此方向相關，但多數試驗是以荷爾蒙replacement組合（含雌激素）進行，黃體素的單獨貢獻難以區分。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：子宮內膜異位症、子宮內膜癌、停經後骨質疏鬆（香港許可證未提供核准適應症文字） |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L2 |
| 香港上市 | 上市中（有效許可證 9 張／共 9 張） |
| 許可證數 | 9 張（有效 9 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知的生理學，黃體素是月經週期中與雌激素相對應的荷爾蒙，參與調控下視丘—腦下垂體—卵巢軸，並控制子宮內膜的增生與蛻膜化。

在雌激素充足的次發性閉經，給予黃體素後停藥可誘發子宮內膜剝落（黃體素挑戰試驗），因此黃體素已被用於閉經的診斷與治療。在低雌激素型閉經（如運動員、神經性厭食症），則常採用雌激素加黃體素的替代療法，以保護骨骼與子宮內膜。

因此這個預測在生物學上合理，也與既有臨床實務一致。但需注意，現有試驗多為雌激素合併黃體素的方案，黃體素本身的療效貢獻常被混淆。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | 完成 | 121 | 年輕運動員停經的身體組成與荷爾蒙差異；比較經皮或口服雌激素對骨密度的影響 |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | 完成 | 110 | 神經性厭食症青少女，評估荷爾蒙替代對骨量的影響 |
| [NCT03740204](https://clinicaltrials.gov/study/NCT03740204) | Phase 2 | 進行中（不再招募） | 120 | 經皮雌二醇加週期性黃體素 vs 安慰劑，評估進食障礙者的認知彈性與獎賞處理，尚無結果 |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | 完成 | 29 | 功能性下視丘閉經年輕女性的心血管風險與發炎指標 |

## 文獻證據

下列文獻多為綜述，沒有以黃體素治療閉經的隨機對照試驗。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Rev Endocr Metab Disord | 口服微粒化黃體素在內分泌的診斷與治療用途 |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Front Endocrinol | 早發性卵巢功能不全的病因、症狀與治療選項 |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | 子宮內膜異位症荷爾蒙治療的內分泌背景 |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | 停經後陰道出血的臨床處置 |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Semin Reprod Med | 子宮內黏連（Asherman 症候群）可表現為閉經 |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | Am Fam Physician | 閉經的評估流程 |
| [8865137](https://pubmed.ncbi.nlm.nih.gov/8865137/) | 1996 | Review | Maturitas | 荷爾蒙替代療法的臨床益處與副作用 |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | 未分類 | Gynecol Endocrinol | 排卵的神經內分泌控制，下視丘衰竭可導致無排卵或閉經 |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | 未分類 | South Med J | 原發性卵巢功能不全常伴隨次發性閉經，需荷爾蒙替代 |
| [26062108](https://pubmed.ncbi.nlm.nih.gov/26062108/) | 2015 | 未分類 | Gynecol Endocrinol | 三種低劑量雌二醇/黃體素每月注射劑型治療更年期症狀 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44527 | CRINONE VAGINAL GEL 8% | 陰道凝膠 | 未提供 |
| HK-34022 | PROGESTOGEL GEL 1% | 凝膠 | 未提供 |
| HK-64210 | LUTINUS VAGINAL TABLETS 100MG | 陰道錠 | 未提供 |
| HK-61091 | UTROGESTAN VAGINAL CAP 200MG | 陰道膠囊 | 未提供 |
| HK-51916 | ENDOMETRIN VAGINAL TAB 100MG | 陰道錠 | 未提供 |

目前共有 9 張許可證，均為單一成分製劑，狀態皆為有效；此處僅列出前 5 張。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：高血壓、肝衰竭、肝病、癲癇、卟啉症、腎臟病、膽囊疾病、高血糖、糖尿病、氣喘、系統性紅斑性狼瘡、甲狀腺功能低下、高三酸甘油脂血症、焦慮症、物質濫用或依賴等。
- **藥物交互作用**：資料庫共記錄 100 筆，列出的多為中度等級，主要涉及降血糖藥物（如 Metformin、Pioglitazone、Glimepiride、Semaglutide、胰島素類）以及 Aprepitant、Clarithromycin 等。使用時需留意血糖變化。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 黃體素用於閉經在生理上合理，並已是內分泌臨床實務的一部分，且有 1 個已完成的 Phase 3 試驗與 1 個 Phase 2/3 試驗針對閉經族群。
- 但這些試驗多為雌激素合併方案，黃體素的獨立療效尚未釐清，且缺乏仿單層級的安全性資料與作用機轉資料。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字
- 補充作用機轉資料
- 設計或尋找黃體素單獨使用（如黃體素挑戰試驗）於閉經的對照研究
- 針對高血壓、肝腎疾病、糖尿病等族群訂定安全性監測計畫

## 其他預測適應症（供參考）

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 乳房纖維囊腫病 | 0.9998 | L4 | 研究問題（僅有間接文獻，無臨床試驗） |
| 良性乳腺發育不良 | 0.9998 | L4 | 研究問題（與上項為同一臨床實體，不宜視為獨立證據） |
| 雙側腎發育不全 | 0.9997 | L5 | Hold（無可信機轉，高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病學到的相似性，而非生物學證據） |
| 腎發育不全 | 0.9997 | L5 | Hold（僅有一項多囊腎小鼠的前臨床研究，屬不同疾病） |
| 乳房頂漿腺病 | 0.9996 | L5 | Hold |
| 乳房鈍性導管腺病 | 0.9996 | L5 | Hold（無試驗亦無文獻） |

上表中乳房纖維囊腫病與良性乳腺發育不良雖有文獻討論荷爾蒙與病程的關聯，但沒有直接研究黃體素治療的證據，依本報告的證據規則，嚴格而言應視為 L5。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

