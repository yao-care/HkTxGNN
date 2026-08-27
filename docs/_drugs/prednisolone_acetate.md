---
layout: default
title: Prednisolone Acetate
parent: 高證據等級 (L1-L2)
nav_order: 411
evidence_level: L2
indication_count: 5
---

# Prednisolone Acetate
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Prednisolone Acetate：原適應症資料缺口 → 乳突性結膜炎（Papillary Conjunctivitis）

## 一句話總結

Prednisolone Acetate（DrugBank DB15566）目前缺乏完整的原適應症與作用機轉資料。
TxGNN 模型在結膜炎相關疾病群組中給出多個高分預測，其中證據基礎最扎實的是**乳突性結膜炎 (Papillary Conjunctivitis)**，
目前有 **2 個臨床試驗**（含 1 個已完成的 Phase 4 研究）和 **6 篇文獻**支持這個方向，
但因安全性仿單資料完全缺失（Blocking 等級資料缺口），暫無法完成初步安全性評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（DrugBank 與香港藥證資料均未提供，見 DG001/DG002） |
| 預測新適應症 | 乳突性結膜炎 (Papillary Conjunctivitis) |
| TxGNN 預測分數 | 99.72%（rank 5814） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

> 補充說明：TxGNN 同時針對此藥物預測出另外 4 個結膜炎相關適應症（parasitic conjunctivitis、serous conjunctivitis except viral、chronic follicular conjunctivitis、conjunctival folliculosis），分數皆與上表接近（約 99.7%）。但這些候選的證據等級為 L3–L5、決策階段皆為 S0/S1、建議一律為 Hold，且部分機轉關聯薄弱甚至存在潛在惡化風險（詳見下節）。因此本報告聚焦於證據品質最高的乳突性結膜炎。

---

## 為什麼這個預測合理？

目前缺乏 Prednisolone Acetate 詳細的作用機轉（MOA）資料（DG002，資料缺口）。根據已知的藥理類別，該藥屬於糖皮質激素（corticosteroid）眼用製劑成分，此類別藥物在眼科領域已廣泛用於各種發炎性結膜/角膜疾病。

由於原適應症資料同樣缺失，無法直接比較原適應症與新適應症之間的相似性；這也是本次評估的一項重要限制。

就乳突性結膜炎本身而言，其核心病理為結膜肥大細胞／嗜酸性球媒介之第一／四型過敏發炎反應（涵蓋巨乳頭狀結膜炎、春季角結膜炎等表現型）。糖皮質激素透過抑制磷脂酶 A2、降低前列腺素／白三烯生成，以及抑制發炎細胞浸潤，是此類疾病臨床標準治療的一環，機轉上直接且成熟。不過需注意，本組證據多來自同類藥物 Loteprednol Etabonate（一種 site-active 皮質類固醇），而非 Prednisolone Acetate 專一性研究資料，兩者雖同屬糖皮質激素，仍建議取得 Prednisolone Acetate 專一性證據以強化結論。

相較之下，其他 4 個預測適應症的機轉關聯明顯較弱：例如 parasitic conjunctivitis（寄生蟲性結膜炎）的首要治療為外科移除病灶，局部免疫抑制對寄生蟲感染反而存在惡化風險；chronic follicular conjunctivitis 若病因為活動性病毒或披衣菌感染，單用類固醇有掩蓋感染徵象之疑慮；其餘 2 個適應症則完全無臨床試驗或文獻支持，僅有模型預測分數。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01437982](https://clinicaltrials.gov/study/NCT01437982) | Phase 4 | 已完成 | 140 | Lotemax（loteprednol etabonate 0.5%）眼用懸液上市後監測研究，評估治療乳突性結膜炎相關發炎之安全性與有效性，屬同類皮質類固醇之真實世界證據 |
| [NCT04705584](https://clinicaltrials.gov/study/NCT04705584) | NA | 狀態不明 | 180 | 比較局部免疫抑制劑（Cyclosporine A 2% vs Tacrolimus 0.3%）用於難治性春季角結膜炎，作為類固醇之替代方案；試驗狀態未知，證據力較弱 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26984315](https://pubmed.ncbi.nlm.nih.gov/26984315/) | 2016 | Review | Advances in Therapy | 探討局部皮質類固醇（含 Loteprednol Etabonate）治療眼部發炎時對眼壓的影響，及長期使用之安全性考量 |
| [18020605](https://pubmed.ncbi.nlm.nih.gov/18020605/) | 1998 | Review | BioDrugs | Loteprednol Etabonate 於眼部發炎管理之臨床潛力綜述，說明「軟性藥物」設計降低全身性副作用之機轉 |
| [9713785](https://pubmed.ncbi.nlm.nih.gov/9713785/) | 1998 | Cohort/Longitudinal Study | Journal of Glaucoma | 長期使用 Loteprednol Etabonate 治療巨乳頭狀結膜炎等疾病時，眼壓上升發生率之追蹤研究 |
| [12917176](https://pubmed.ncbi.nlm.nih.gov/12917176/) | 2003 | Pilot Study | Ophthalmology | 局部 Cyclosporine A 0.5% 作為上緣角結膜炎（SLK）新治療選項之初步試驗，可作為類固醇替代方案之對照參考 |
| [29260110](https://pubmed.ncbi.nlm.nih.gov/29260110/) | 2017 | Case Series | American Journal of Ophthalmology Case Reports | 藥物治療無效之巨乳頭狀結膜炎（GPC）病例，比較合併羊膜移植與否之手術切除結果 |
| [18724159](https://pubmed.ncbi.nlm.nih.gov/18724159/) | 2008 | Case Report | Cornea | 描述一例與菊池氏病（Kikuchi-Fujimoto disease）相關之乳突性結膜炎個案 |

---

## 香港上市資訊

目前 Prednisolone Acetate 於香港**未上市**，無任何許可證登記，故無許可證資訊可列出。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 需特別注意：目前完全缺乏 Prednisolone Acetate 之仿單警語、禁忌症及藥物交互作用資料（DG001，Blocking 等級資料缺口）。此缺口直接影響能否進入 S1 安全性初評，是本次評估決策的主要限制因素。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 乳突性結膜炎為 5 個預測適應症中證據等級最高者（L2，含 1 個已完成的 Phase 4 研究與 6 篇文獻），機轉上具合理性，但證據多來自同類藥物 Loteprednol Etabonate，非 Prednisolone Acetate 專一性資料。
- 安全性仿單資料完全缺失（DG001，Blocking），依規範無法完成 S1 安全性初評，此為推進的硬性阻礙。
- 藥品目前未於香港上市，無許可證可供銜接臨床應用途徑。

**若要推進需要：**
- 取得 Prednisolone Acetate 完整仿单警語、禁忌症與藥物交互作用資料（解除 DG001，Blocking）
- 補充 DrugBank 或原廠之詳細作用機轉（MOA）資料（解除 DG002）
- 針對 Prednisolone Acetate（而非同類藥物 Loteprednol Etabonate）檢索專一性臨床試驗或文獻，強化證據強度
- 評估香港藥證申請路徑或現行進口用藥管道
- 其餘 4 個結膜炎相關預測適應症證據薄弱或機轉存疑，建議暫不列入後續追蹤，除非取得新的臨床或文獻證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

