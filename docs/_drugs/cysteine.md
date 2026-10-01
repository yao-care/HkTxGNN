---
layout: default
title: Cysteine
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 7
---

# Cysteine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cysteine：從（原適應症未載明）到乾眼症

## 一句話總結

Cysteine（半胱胺酸）是含硫胺基酸，也是麩胱甘肽的前驅物，目前資料中未載明其原適應症。
TxGNN 模型預測它可能對**乾眼症 (Dry Eye Syndrome)** 有效，
目前有 **6 個登記試驗**（其中僅 1–2 個與眼部或 NAC 相關）和 **20 篇文獻**，其中的隨機對照證據多數針對 N-acetylcysteine (NAC) 或硫醇化衍生物，並非 L-cysteine 本身。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未載明（香港許可證資料皆無適應症文字） |
| 預測新適應症 | 乾眼症 (Dry Eye Syndrome) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L2（僅就 NAC／衍生物而言；L-cysteine 本身證據較弱） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold（研究問題階段，待釐清） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cysteine 是硫醇供體與麩胱甘肽前驅物，其乙醯化形式 N-acetylcysteine (NAC) 已有廣泛研究。

乾眼症的病程與眼表氧化壓力（ROS）、發炎及淚膜黏液異常有關。NAC 的可能作用包括：清除自由基、抗發炎、分解淚膜黏蛋白的雙硫鍵（黏液溶解），另有硫醇化聚合物（thiomers）可增加黏膜附著。這些機轉與乾眼症病理有合理連結。

需注意：隨機對照證據多來自 NAC 或其衍生物（如 chitosan-NAC 滴眼液），並非 L-cysteine 本身。TxGNN 分數高，但屬模型預測，不是臨床證明。

---

## 臨床試驗證據

與乾眼症直接相關的登記試驗很有限，其餘多為搜尋比對的雜訊。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04793646](https://clinicaltrials.gov/study/NCT04793646) | N/A | 完成 | 60 | 隨機雙盲，NAC 治療原發性乾燥症候群的乾燥症狀；最直接相關，但眼部終點需再確認 |
| [NCT04440280](https://clinicaltrials.gov/study/NCT04440280) | Phase 2 | 招募中 | 45 | NAC 滴眼液用於福斯氏角膜內皮失養症，降低氧化壓力（不同疾病，僅支持眼部抗氧化理由） |
| [NCT01424033](https://clinicaltrials.gov/study/NCT01424033) | Phase 2/3 | 終止 | 5 | 口服 NAC 用於結締組織病相關間質性肺病，非眼部適應症 |
| [NCT01064830](https://clinicaltrials.gov/study/NCT01064830) | Phase 2 | 完成 | 21 | 外用 cyclosporine 用於脆甲症，與 cysteine 無直接關係 |
| [NCT03525678](https://clinicaltrials.gov/study/NCT03525678) | Phase 2 | 完成 | 221 | 多發性骨髓瘤 belantamab 劑量比較，疑為搜尋比對雜訊 |
| [NCT04162210](https://clinicaltrials.gov/study/NCT04162210) | Phase 3 | 進行中（不招募） | 325 | 多發性骨髓瘤 belantamab 對比 Pom/Dex，與本案無關 |
| [NCT03544281](https://clinicaltrials.gov/study/NCT03544281) | Phase 1/2 | 完成 | 153 | 多發性骨髓瘤 belantamab 合併療法，與本案無關 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39360368](https://pubmed.ncbi.nlm.nih.gov/39360368/) | 2024 | RCT | Clin Exp Rheumatol | 隨機安慰劑對照雙盲，評估 NAC 改善乾燥症候群的乾燥症狀 |
| [28441068](https://pubmed.ncbi.nlm.nih.gov/28441068/) | 2017 | RCT | J Ocul Pharmacol Ther | Chitosan-NAC 滴眼液對乾眼症患者淚膜厚度的影響（隨機雙盲） |
| [34339721](https://pubmed.ncbi.nlm.nih.gov/34339721/) | 2022 | Review | Surv Ophthalmol | 局部 NAC 在眼科治療的角色：機轉、應用與不良反應（106 篇文獻） |
| [24993428](https://pubmed.ncbi.nlm.nih.gov/24993428/) | 2014 | Review | J Control Release | 硫醇化聚合物（thiomers）的黏膜附著特性與應用 |
| [16334742](https://pubmed.ncbi.nlm.nih.gov/16334742/) | 2005 | 臨床比較 | Acta Med Croatica | 局部乙醯半胱胺酸與人工淚液治療乾眼症的比較 |
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | 前臨床 | Adv Mater | 過氧化氫酶與半胱胺酸修飾殼聚醣的奈米滴眼液用於乾眼症 |
| [39842600](https://pubmed.ncbi.nlm.nih.gov/39842600/) | 2025 | 前臨床 | Int J Biol Macromol | NAC-殼聚醣修飾的 dexamethasone 脂質載體，增進滲透與滯留 |
| [36581034](https://pubmed.ncbi.nlm.nih.gov/36581034/) | 2023 | 前臨床 | Int J Biol Macromol | 硫酸軟骨素-L-半胱胺酸修飾的奈米脂質載體用於乾眼治療 |
| [30025127](https://pubmed.ncbi.nlm.nih.gov/30025127/) | 2018 | 動物模型 | Invest Ophthalmol Vis Sci | 局部黏液溶解劑（NAC）對淚液與眼表的影響，作為黏蛋白缺乏型乾眼模型 |
| [25701684](https://pubmed.ncbi.nlm.nih.gov/25701684/) | 2015 | 機轉研究 | Exp Eye Res | ROS 活化 NLRP3 發炎體，在高滲透壓角膜上皮細胞與乾眼患者中啟動發炎 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58960 | HAKUBI WHITE C TAB | 未載明 | 未載明 |
| HK-36470 | VAMINOLACT I.V. SOLUTION | 未載明 | 未載明 |
| HK-65813 | NUMETA G13% E PRETERM EMULSION FOR INFUSION 300ML | 未載明 | 未載明 |
| HK-65811 | NUMETA G16% E EMULSION FOR INFUSION 500ML | 未載明 | 未載明 |
| HK-65812 | NUMETA G19% E EMULSION FOR INFUSION 1000ML | 未載明 | 未載明 |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉合理，TxGNN 分數高，但有意義的隨機證據來自 NAC 或其衍生物，L-cysteine 本身缺乏乾眼症的直接臨床證據。
- 登記試驗中多數與本案無關，最相關的 NCT04793646 仍需確認其眼部終點。
- 香港現有製劑為口服維他命複方及靜脈營養輸液，與滴眼液劑型不同，路徑相容性尚未評估。

**若要推進需要：**
- 確認 NCT04793646 的納入條件與主要終點是否包含乾眼症或眼表指標。
- 釐清應以 L-cysteine 或 NAC 作為候選成分。
- 評估眼用劑型的開發可行性，以及與現有香港許可證劑型的落差。
- 取得香港衞生署仿單的警語與禁忌資料，以及詳細作用機轉資料。

---

## 其他預測適應症（供參考）

其餘預測適應症證據皆薄弱，建議暫不推進：

| 預測適應症 | TxGNN 分數 | 證據等級 | 決策 | 說明 |
|-----------|-----------|---------|------|------|
| 閉角型青光眼 / 隱角型青光眼（重複條目） | 99.95% / 99.06% | L5 | Hold | 文獻皆為 SPARC 蛋白（名稱含 cysteine），並非藥物證據，疑為關鍵字比對雜訊，建議合併條目 |
| 鼻腔疾病 | 99.88% | L4 | Hold | 僅有 1996 年小型 NAC 合併 tuaminoheptane 的研究，混雜因子多 |
| 急性喉咽炎 | 99.79% | L5 | Hold | 僅有模型預測，無試驗與文獻 |
| 咽炎 | 99.78% | L4 | Hold | 僅有 NAC 扁桃體生物膜的體外研究，屬間接證據 |
| 運動誘發惡性高熱 | 99.26% | L5 | Hold | 無支持證據，且為罕見高急性度疾病 |

---

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

