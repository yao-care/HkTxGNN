---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carfilzomib：從多發性骨髓瘤到黑色素瘤

## 一句話總結

Carfilzomib 是第二代不可逆蛋白酶體抑制劑，以多發性骨髓瘤為核心適應症。
TxGNN 模型預測它可能對**黑色素瘤譜系（Melanoma Spectrum）**有效，共產生 5 個相關預測，最高排名為 **CMM7（皮膚惡性黑色素瘤易感位點 7，99.37%）**。
目前有 **5 篇前臨床文獻**支持黑色素瘤方向，但**無任何臨床試驗登記**，香港亦尚未上市。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 多發性骨髓瘤（依藥物已知用途推斷；Evidence Pack 正式欄位待補） |
| 預測新適應症 | 黑色素瘤譜系（5 個預測；最高排名：CMM7） |
| TxGNN 預測分數 | 99.37%（CMM7，Rank 1） |
| 證據等級 | L5（Ranks 1–4）/ L4（黑色素瘤，Rank 5） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Carfilzomib 透過不可逆地共價結合 26S 蛋白酶體的 20S 催化次單位（chymotrypsin-like activity），阻止腫瘤細胞清除錯誤折疊蛋白，累積的蛋白毒性壓力最終誘發內質網壓力（ER stress）和細胞凋亡。骨髓瘤細胞因持續合成大量免疫球蛋白，對蛋白酶體功能的依賴遠高於正常細胞，這是 Carfilzomib 在血液腫瘤療效的分子基礎。

**黑色素瘤的機轉關聯性**：黑色素瘤細胞同樣具有高蛋白酶體活性，依賴泛素-蛋白酶體系統（UPS）降解促凋亡蛋白（BIM、NOXA、p21）以維持存活訊號。蛋白酶體抑制劑的理論效果包括：(1) 阻止 IκBα 降解 → NF-κB 訊號受阻 → 促凋亡；(2) ER stress 累積 → UPR（未折疊蛋白反應）→ caspase 活化。PMID 33671902 直接以 B16-F1 黑色素瘤細胞株驗證了 Carfilzomib 誘導凋亡的效果（caspase 3/8/9/12 均活化）。

**重要限制與 TxGNN 高分的解讀**：本次 5 個預測均屬黑色素瘤節點集群，高 TxGNN 分數（99.37%–99.03%）主要反映知識圖譜中黑色素瘤節點的高連通性（graph propagation），而非子類型特異性的臨床機轉證據。特別注意：**Rank 1（CMM7）是黑色素瘤易感性遺傳位點，並非獨立疾病分類**，不宜直接作為藥物標靶適應症解讀。固態腫瘤中蛋白酶體抑制劑的臨床轉化率歷史上偏低，主因為藥物穿透固態腫瘤效率不佳與複雜的耐藥機制。

---

## 文獻證據

以下文獻均來自黑色素瘤（Rank 5）預測，為本次 Evidence Pack 中唯一有文獻支撐的適應症。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | 前臨床（In vitro） | Biology | Carfilzomib + Bortezomib 聯用在 B16-F1 黑色素瘤細胞誘導凋亡，caspase 3/8/9/12 均活化 |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | 計算 / In silico | J Biomol Struct Dyn | 多癌症激酶靶點老藥新用分子對接研究，含黑色素瘤在內 10 種癌型 |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | 基礎科學 / 機轉 | Mol Cancer Res | ZAND2a/AIRAP 基因透過 E3 連接酶 cIAP2 調控黑色素瘤細胞存活 |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | 基礎科學 / PROTAC | Leukemia | BRD4-PROTAC 在骨髓瘤模型中透過蛋白酶體降解機轉發揮效果（機轉可類推） |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | 機轉 / 耐藥性 | Matrix Biol | Bortezomib/Carfilzomib 活化 NF-κB 誘導肝素酶表現上升，可能增強腫瘤侵襲性（耐藥警示） |

> **注意**：Ranks 1–4（CMM7、兒科軟腦膜黑色素瘤、葡萄膜黑色素瘤上皮樣型、外陰黑色素瘤）均**無任何臨床試驗或文獻支持**。

---

## 香港上市資訊

Carfilzomib 目前**未在香港上市**，無有效許可證紀錄（共 0 張）。如需評估引進，需先確認是否有其他地區（如美國 FDA、EMA）批准黑色素瘤適應症，再評估香港 EUA 或特殊進口路徑。

---

## 細胞毒性

Carfilzomib 為抗腫瘤藥物（蛋白酶體抑制劑類），以下為相關資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（蛋白酶體抑制劑，Proteasome Inhibitor） |
| 骨髓抑制風險 | 高（血小板減少、嗜中性球減少為主要劑量限制毒性） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類計數）、肝腎功能、心臟功能（LVEF，心臟毒性為已知風險）、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；靜脈注射劑型需專業人員於適當防護條件下配藥 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 所有 5 個預測均屬黑色素瘤節點集群效應，最具機轉支持的「黑色素瘤（Rank 5）」僅有前臨床細胞株研究（L4），無任何人體臨床試驗；Rank 1 的 CMM7 為遺傳易感位點而非疾病本體，不適合直接作為再利用靶點。香港未上市、安全性資料缺口均為 Blocking 級別，現階段不具備進入系統性評估的條件。

**若要推進需要：**
- 補充完整 MOA 資料（DrugBank API 查詢，DG002 修復）
- 取得香港或其他藥監局的完整安全性資料，包括警語、禁忌症、DDI（DG001 修復）
- 確認是否存在針對固態腫瘤（包括黑色素瘤）的 Phase 1/2 臨床試驗（當前查詢結果為零）
- 評估 Carfilzomib 在固態腫瘤中的 PK 可行性（腫瘤滲透率、蛋白結合率、給藥途徑）
- 若考慮兒科軟腦膜黑色素瘤（Rank 2），需先釐清 CNS 穿透性和兒科族群安全性資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

