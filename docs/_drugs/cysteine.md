---
layout: default
title: Cysteine
parent: 高證據等級 (L1-L2)
nav_order: 170
evidence_level: L2
indication_count: 7
---

# Cysteine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **7** 個
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

# Cysteine：從胺基酸前驅物到乾眼症

## 一句話總結

Cysteine（L-半胱氨酸）是人體天然存在的含硫胺基酸，亦是 N-乙醯半胱氨酸（NAC）的直接生物前驅物，具有抗氧化與黏液溶解的雙重特性，目前無正式核准適應症。
TxGNN 模型預測它可能對**乾眼症 (Dry Eye Syndrome)** 有效，
目前有 **7 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式核准適應症（天然胺基酸前驅物） |
| 預測新適應症 | 乾眼症 (Dry Eye Syndrome) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 L-Cysteine 的詳細作用機轉資料。根據已知資訊，L-Cysteine 是含硫胺基酸，在體內可轉化為 N-乙醯半胱氨酸（NAC）並進一步合成谷胱甘肽（GSH）。其核心藥理機轉包含三條路徑：(1) 作為 GSH 前驅物，清除眼表過量活性氧（ROS），減輕角結膜上皮氧化損傷；(2) 透過斷裂黏蛋白二硫鍵，降低淚液黏稠度，改善黏液纖毛清除功能；(3) 與殼聚糖形成硫醇共軛物（chitosan-cysteine），增強眼表滯留性與保濕效果。

乾眼症的核心病理機制之一正是淚液高滲透壓所誘發的 ROS 過度生成及後續炎症反應（PMID 25701684），與 Cysteine／NAC 的抗氧化及黏液溶解路徑高度吻合。多項眼表藥物遞送研究（PMID 36581034、39842600）更直接採用 L-Cysteine 接枝殼聚糖作為奈米載體表面修飾材料，用於乾眼症治療，顯示 L-Cysteine 本身具備眼表應用的結構基礎。

需特別說明：現有最強臨床試驗證據主要來自 NAC 相關研究，而非 L-Cysteine 本身。NAC 為 Cysteine 的直接醯化衍生物，兩者藥理路徑密切相關，但臨床應用有所區別。推進時需審慎確認 L-Cysteine 與 NAC 之間的臨床等效轉換路徑。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04793646](https://clinicaltrials.gov/study/NCT04793646) | 隨機對照（NA） | 完成 | 60 | 前瞻性隨機雙盲安慰劑對照研究，直接評估 NAC 治療 Sjögren 氏症相關乾燥症狀，與本適應症**高度相關**；NAC 為 L-Cysteine 直接衍生物，藥效轉換路徑清晰 |
| [NCT04440280](https://clinicaltrials.gov/study/NCT04440280) | Phase 2 | 招募中 | 45 | 局部 NAC 滴眼液針對 Fuchs 角膜內皮營養不良症靶向 ROS 生成，機轉與乾眼症抗氧化路徑吻合，尚未完成 |
| [NCT01424033](https://clinicaltrials.gov/study/NCT01424033) | Phase 2/3 | 終止 | 5 | NAC 用於結締組織病合併間質性肺病（CTD-ILD）耐受性評估，已終止且樣本極少，與乾眼關聯性間接 |
| [NCT01064830](https://clinicaltrials.gov/study/NCT01064830) | Phase 2 | 完成 | 21 | Cyclosporine 0.05% 眼科製劑研究，摘要中提及 cysteine 缺乏與脆甲症關聯，乾眼直接相關性低 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28441068](https://pubmed.ncbi.nlm.nih.gov/28441068/) | 2017 | RCT | J Ocular Pharmacol Ther | 殼聚糖-NAC（C-NAC）滴眼液在乾眼症患者中顯著增加淚膜厚度，隨機雙盲對照研究 |
| [39360368](https://pubmed.ncbi.nlm.nih.gov/39360368/) | 2024 | RCT | Clin Exp Rheumatology | NAC 治療 Sjögren 氏症乾燥症狀之隨機安慰劑對照雙盲研究，直接驗證乾眼療效 |
| [34339721](https://pubmed.ncbi.nlm.nih.gov/34339721/) | 2022 | Review | Survey of Ophthalmology | 系統性回顧局部 NAC 在眼科治療的角色，涵蓋 106 篇文獻，詳述機轉、臨床應用及不良反應 |
| [16334742](https://pubmed.ncbi.nlm.nih.gov/16334742/) | 2005 | Clinical | Acta Medica Croatica | 局部乙醯半胱氨酸與人工淚液比較研究，NAC 作為黏液溶解劑有效緩解乾眼症狀 |
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclinical | Advanced Materials | 半胱氨酸修飾殼聚糖（CS-Cys）與過氧化氫酶自組裝奈米製劑滴眼液，ROS 清除路徑治療乾眼症 |
| [39842600](https://pubmed.ncbi.nlm.nih.gov/39842600/) | 2025 | Preclinical | Int J Biol Macromolecules | NAC-殼聚糖共軛修飾地塞米松奈米結構脂質載體，顯著提升角膜通透性與乾眼症療效 |
| [36581034](https://pubmed.ncbi.nlm.nih.gov/36581034/) | 2023 | Preclinical | Int J Biol Macromolecules | **直接使用 L-Cysteine** 接枝硫酸軟骨素修飾陽離子奈米脂質載體，增強角膜通透性與滯留性用於乾眼治療 |
| [25701684](https://pubmed.ncbi.nlm.nih.gov/25701684/) | 2015 | Molecular | Exp Eye Research | 淚液高滲透壓透過 ROS 活化 NLRP3 炎症小體介導乾眼炎症，支持抗氧化治療機轉的理論基礎 |
| [39359484](https://pubmed.ncbi.nlm.nih.gov/39359484/) | 2024 | Preclinical | Drug Des Dev Ther | NAC 建立黏液缺乏型乾眼動物模型，環糊精聚合物增強 Rebamipide 療效，確認 NAC 在乾眼研究的工具性角色 |
| [24993428](https://pubmed.ncbi.nlm.nih.gov/24993428/) | 2014 | Review | J Controlled Release | 硫醇化聚合物（Thiomers）機轉回顧，Cysteine-糖聚合物共軛物顯著提升黏膜附著性，支持眼表藥物遞送應用 |

---

## 香港上市資訊

L-Cysteine（DB00151）目前在香港**無已登記藥物許可證**，市場狀態為未上市。如需推進本適應症的臨床應用，須先進行香港衛生署或其他主要藥監機構的新藥申請（NDA）或適應症外使用（Off-label Use）評估。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有 1 個完成的前瞻性隨機雙盲安慰劑對照臨床研究（NCT04793646，N=60）直接支持 NAC 治療 Sjögren 相關乾眼症，加上 2 篇 RCT 文獻（PMID 28441068、39360368）及多項前臨床研究佐證；L-Cysteine 作為 NAC 的直接生物前驅物，機轉可信度充分。然而核心臨床證據為 NAC 而非 L-Cysteine 本身，加之香港尚無許可，需在明確 L-Cysteine 本身的等效性後方可全力推進。

**若要推進需要：**
- 補充 L-Cysteine 本身（有別於 NAC 衍生物）的藥理作用機轉（MOA）資料
- 確認 L-Cysteine 與 NAC 之間的臨床等效轉換路徑與劑量換算關係
- 評估最適給藥途徑（局部滴眼液 vs. 口服），確認眼部生物利用度
- 香港藥物許可策略評估，包含新藥申請或適應症外使用框架
- 制定完整安全性監測計畫，特別是長期局部眼科給藥的耐受性資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

