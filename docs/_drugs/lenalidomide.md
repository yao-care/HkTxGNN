---
layout: default
title: Lenalidomide
parent: 高證據等級 (L1-L2)
nav_order: 518
evidence_level: L2
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "LENALIDOMIDE"
predicted_indications: ["myeloid leukemia", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts"]
description: "Lenalidomide：預測新適應症為骨髓性白血病 (myeloid leukemia)（證據等級 L2）。香港藥劑製品註冊：8 張（有效 8 張）"
---

# Lenalidomide
{: .fs-9 }

證據等級: **L2** | 預測適應症: **4** 個
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

## Lenalidomide: 骨髓性白血病 (myeloid leukemia)
{: .text-alpha }

## 一句話總結

Lenalidomide（來那度胺）原本用於漿細胞骨髓瘤、被套細胞淋巴瘤、B 細胞腫瘤、淋巴肉瘤及骨髓增生異常症候群（MDS）。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，
目前有 **46 個臨床試驗**和 **19 篇文獻**與此方向相關，但多數為早期、小型研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 骨髓性白血病 (myeloid leukemia) |
| TxGNN 預測分數 | 0.9949 |
| 證據等級 | L2 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Proceed with Guardrails（限於研究性質） |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Lenalidomide 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Lenalidomide是thalidomide的類似物，具有免疫調節、抗血管生成及抗腫瘤特性。Lenalidomide的細胞活性是通過其標靶cereblon介導的；cereblon是cullin環E3泛素連接酶複合物的組成部分。」英文原文："Lenalidomide is an analogue of thalidomide with immunomodulatory, antiangiogenic, and antineoplastic properties. Cellular activities of lenalidomide are mediated through its target cereblon, a component of a cullin ring E3 ubiquitin ligase enzyme complex."（[DailyMed: Revlimid (lenalidomide) prescribing information, Celgene Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5fa97bf5-28a2-48f1-8955-f56012d296be)，版本日期 2023-03-24；查閱日期 2026-11-19）。依文獻與模型推論，Lenalidomide 是 cereblon E3 連接酶調節劑，會促使 IKZF1/IKZF3 降解；在 del(5q) MDS 中，CK1α 的降解是療效關鍵。它同時具有免疫調節作用，例如活化 NK 細胞與 T 細胞。

原適應症已涵蓋 MDS，而 MDS 與急性骨髓性白血病（AML）同屬骨髓性腫瘤，MDS 約三分之一會轉化為 AML。因此在生物學上有合理的連結。

不過，這個機轉在非 del(5q) 的 AML 中較不明確，需要依染色體異常分層來判斷哪些病人可能受益。

---

## 臨床試驗證據

資料中共有 46 個相關試驗，以下列出最相關的 10 個（依相關性分級 A、B 優先）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | 完成 | 29 | 高風險 AML 緩解後的 Lenalidomide 維持治療（單臂、小型） |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | 完成 | 27 | 單藥 Lenalidomide 用於復發/難治性 AML 或伴 5 號染色體異常的高風險 MDS |
| [NCT00831766](https://clinicaltrials.gov/study/NCT00831766) | Phase 1/2 | 完成 | 51 | Idarubicin + Cytarabine 後接 Lenalidomide，用於 MDS (RAEB-2) 或未治療 AML |
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Phase 1/2 | 完成 | 37 | Lenalidomide + Azacitidine 用於晚期 MDS，族群可能混合 AML/MDS |
| [NCT01681537](https://clinicaltrials.gov/study/NCT01681537) | Phase 1 | 完成 | 36 | Lenalidomide + MEC 化療用於 AML 再誘導，主要為安全性與劑量資料 |
| [NCT01578954](https://clinicaltrials.gov/study/NCT01578954) | Phase 1 | 完成 | 20 | 60 歲以上 AML 再誘導/鞏固後的 Lenalidomide 劑量探索與維持 |
| [NCT01254578](https://clinicaltrials.gov/study/NCT01254578) | Phase 1 | 完成 | 17 | 異體移植後 Lenalidomide 維持，需留意移植特有的 GVHD 風險 |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | 完成 | 88 | 比較高劑量 Lenalidomide、Azacitidine 序貫 Lenalidomide 與 Azacitidine，用於 65 歲以上新診斷 AML |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Phase 2 | 完成 | 120 | 高齡 AML 首次緩解後，Lenalidomide 與 Azacitidine 交替維持治療 |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Phase 3 | 未知 | 60 | 依 MRD 監測，Azacitidine + Lenalidomide 用於高齡或不適合強化治療 AML 的維持治療 |

其餘試驗多為 Phase 1 或 Phase 1/2 的小型研究，另有 Phase 3 試驗 NCT00843882（MDS，Lenalidomide 加或不加 epoetin alfa），目前仍進行中。資料中沒有已完成的 Phase 3 RCT。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | 回顧 Lenalidomide 作為 AML 新療法，已有在高風險 MDS 與 AML 的試驗 |
| [32899586](https://pubmed.ncbi.nlm.nih.gov/32899586/) | 2020 | 回顧性文章 | Cancers | 免疫調節藥物（IMiDs）在 AML 治療中的角色 |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | 機轉研究 | Cell Mol Biol Lett | KDM5C 透過穩定 cereblon 提高 AML 細胞對 Lenalidomide 的敏感性 |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | Am J Hematol | MDS 診斷、風險分層與處置更新 |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | MDS 的臨床決策與治療 |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | MDS 總覽，約三分之一病人會進展為 AML |
| [29795386](https://pubmed.ncbi.nlm.nih.gov/29795386/) | 2018 | 回顧性文章 | Blood Cancer J | MDS 治療流程 |
| [17488990](https://pubmed.ncbi.nlm.nih.gov/17488990/) | 2007 | 回顧性文章 | J Clin Oncol | 高齡 AML 與 MDS 的治療考量 |
| [22483153](https://pubmed.ncbi.nlm.nih.gov/22483153/) | 2012 | 回顧性文章 | Curr Cancer Drug Targets | AML 新興藥物 |
| [20416083](https://pubmed.ncbi.nlm.nih.gov/20416083/) | 2010 | 會議摘要 | J Hematol Oncol | 2009 年 ASH 會議 AML 新藥與新方案重點 |

資料中沒有 RCT 層級的文獻直接證明 Lenalidomide 對 AML 有效。

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-62180 | REVLIMID CAPSULES 25MG (SWITZERLAND) | 單一成分 | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD | 有效 |
| HK-62181 | REVLIMID CAPSULES 15MG (SWITZERLAND) | 單一成分 | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD | 有效 |
| HK-62182 | REVLIMID CAPSULES 10MG (SWITZERLAND) | 單一成分 | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD | 有效 |
| HK-62183 | REVLIMID CAPSULES 5MG (SWITZERLAND) | 單一成分 | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD | 有效 |
| HK-68893 | LENALIDOMIDE SANDOZ CAPSULES 10MG | 單一成分 | SANDOZ HONG KONG LIMITED | 有效 |

上表列出其中 5 張（共 8 張）。

<!-- licenses:end -->

共 8 張有效許可證（Bristol-Myers Squibb 4 張、Sandoz 4 張），此處列出 5 張。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫調節藥物（IMiD，cereblon E3 連接酶調節劑），非傳統細胞毒性化療 |
| 骨髓抑制風險 | 高。知識圖譜顯示血小板低下、嗜中性白血球低下與顆粒球缺乏為禁忌相關疾病 |
| 監測項目 | 定期 CBC（含分類與血小板）、腎功能 |
| 處置防護 | 請參考原廠仿單的處置與風險管理規範 |

致吐性分級與其他細胞毒性細節請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**：血小板低下、嗜中性白血球低下、顆粒球缺乏、肺栓塞、腎功能不全、癌症、胚胎瘤。這些來自知識圖譜，並非仿單文字。
- **藥物交互作用**：共查詢到 100 筆，主要列出如下：
  - 重度：Rosuvastatin、Simvastatin
  - 中度：Eliglustat、Naltrexone
  - 其餘多為等級不明（如 Metformin、Omeprazole、Morphine、Prednisone 等）

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個 Phase 2 試驗直接在 AML 或高風險 MDS 中測試 Lenalidomide，加上 MDS 已是原適應症，機轉上具合理性。但證據多為單臂、小型研究，沒有已完成的 Phase 3 RCT，只適合作為研究性問題推進，不宜直接臨床推廣。
- 藥物已在香港上市（8 張許可證），取得性不是障礙；但血球低下風險對 AML 這類本身骨髓功能受損的族群尤其需要留意。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症，以完成安全性篩選
- 補充 DrugBank 的作用機轉資料
- 依細胞遺傳學（如 del(5q)、非 del(5q)）分層，找出可能受益的 AML 族群
- 詳細審視 Phase 2 試驗（如 NCT02126553、NCT00360672）的反應率與存活結果
- 制定血球監測與劑量調整計畫

**其他預測適應症的補充說明：**
- 未分類骨髓增生異常症候群（L3）：僅有世代研究與病例報告，建議視為研究問題，可依 del(5q) 狀態分層。
- 兒童難治性血球低下（L3）：唯一試驗為兒童實體瘤的 Phase 1，機轉連結薄弱，建議 Hold。
- 再生不良性貧血（L3）：文獻多與骨髓瘤、淋巴瘤相關，缺乏直接證據，建議 Hold。
- 嚴重先天性低色素貧血伴環狀鐵粒幼細胞（L5）：僅有模型預測，病因為遺傳性，建議 Hold。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Revlimid (lenalidomide) prescribing information, Celgene Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5fa97bf5-28a2-48f1-8955-f56012d296be) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

