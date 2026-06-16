---
layout: default
title: Fludarabine
parent: 高證據等級 (L1-L2)
nav_order: 322
evidence_level: L2
indication_count: 10
---

# Fludarabine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Fludarabine：從 B 細胞血液惡性腫瘤到漿細胞骨髓瘤

## 一句話總結

Fludarabine 是一種嘌呤核苷類似物，原核准用於慢性淋巴性白血病（CLL）、毛細胞白血病及惰性淋巴瘤的治療，香港目前尚未有正式藥品許可登記。
TxGNN 模型預測它可能對**漿細胞骨髓瘤（Plasma Cell Myeloma）** 有效，
目前有超過 **50 個臨床試驗**佐證此方向，惟針對性文獻搜尋尚未找到直接相關文獻。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | B 細胞慢性淋巴性白血病、毛細胞白血病、惰性淋巴瘤（國際核准，香港未登記） |
| 預測新適應症 | 漿細胞骨髓瘤（Plasma Cell Myeloma） |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Fludarabine 為嘌呤核苷類似物，透過競爭性抑制 DNA 聚合酶與核糖核苷酸還原酶，阻斷 DNA 合成並誘導增殖細胞凋亡。此機轉對漿細胞（多發性骨髓瘤的惡性前驅細胞）具備直接細胞毒性。2007 年一項體外及動物實驗（PMID 17976186）已直接確認：Fludarabine 能有效抑制骨髓瘤細胞株 RPMI8226 的增殖，並同步降低 Akt 磷酸化，顯示其抗腫瘤活性不僅限於免疫調控層面。

漿細胞骨髓瘤與 CLL、惰性淋巴瘤同屬 B 細胞譜系惡性腫瘤，在免疫表型（CD19/CD38/CD138 軸）與信號傳導路徑（PI3K/Akt、NF-κB）上高度重疊。Fludarabine 在 CLL 中已驗證有效，延伸至同源 B 細胞來源的漿細胞腫瘤具有合理的生物學根據。

目前在臨床上，Fludarabine 在骨髓瘤最廣泛的應用是作為異體造血幹細胞移植（allo-SCT）的減強度預處理（RIC）核心藥物，與美法蘭（Melphalan）、白消安（Busulfan）聯合使用；近年更成為 CAR-T 細胞療法前淋巴清除（lymphodepletion）的標準配方。這些應用已累積大量 Phase 1/2 完成的臨床試驗，代表 Fludarabine 在骨髓瘤治療生態系統中已確立的功能性地位。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01453101](https://clinicaltrials.gov/study/NCT01453101) | Phase 2 | 完成 | 54 | Fludarabine + Melphalan + Bortezomib 作為多發性骨髓瘤 allo-HSCT 條件化方案，假設優於歷史對照 Flu/Mel 單用 |
| [NCT00006251](https://clinicaltrials.gov/study/NCT00006251) | Phase 1/2 | 完成 | 21 | Fludarabine + 低劑量 TBI 誘導混合造血嵌合，招募漿細胞骨髓瘤患者，評估 RIC 直接應用 |
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | 完成 | 20 | Fludarabine + Methoxyamine（TRC102）DNA 修復抑制協同方案，用於含骨髓瘤之復發/難治性血液惡性腫瘤 |
| [NCT01408563](https://clinicaltrials.gov/study/NCT01408563) | Phase 2 | 完成 | 33 | Fludarabine + Melphalan + 低劑量 TBI 雙臍帶血移植，適用進展期血液惡性腫瘤含骨髓瘤 |
| [NCT00802568](https://clinicaltrials.gov/study/NCT00802568) | Phase 2 | 完成 | 48 | Fludarabine + Busulfan + ATG 減強度條件化後異體幹細胞移植治療多發性骨髓瘤 |
| [NCT01503242](https://clinicaltrials.gov/study/NCT01503242) | Phase 1 | 完成 | 15 | ⁹⁰Y 放射標記抗 CD45 單抗（BC8）+ Fludarabine + TBI 後接異體 PBSC 移植，直接針對多發性骨髓瘤 |
| [NCT00054353](https://clinicaltrials.gov/study/NCT00054353) | Phase 1/2 | 完成 | 16 | Fludarabine + Melphalan + TBI 減強度預處理，HLA 配對相關/非相關供體 PBSCT 治療多發性骨髓瘤 |
| [NCT07477912](https://clinicaltrials.gov/study/NCT07477912) | Phase 1/2 | 招募中 | 30 | Anti-BCMA CAR-T 治療 R/R 多發性骨髓瘤，Fludarabine 作為標準淋巴清除前處理，代表 CAR-T 時代的應用 |
| [NCT06196255](https://clinicaltrials.gov/study/NCT06196255) | Phase 1/2 | 招募中 | 20 | Anti-FcRL5 CAR-T 用於復發/難治性多發性骨髓瘤，Fludarabine + Cyclophosphamide 淋巴清除 |
| [NCT05020444](https://clinicaltrials.gov/study/NCT05020444) | Phase 1 | 招募中 | 18 | TriPRIL CAR-T 細胞治療復發/難治性骨髓瘤，Fludarabine + Cyclophosphamide 為標準淋巴清除方案 |

---

## 文獻證據

目前無相關文獻（針對漿細胞骨髓瘤的直接 PubMed 搜尋未返回結果）。

> **補充說明**：在相鄰適應症「惰性漿細胞骨髓瘤」的搜尋中，發現一篇高相關性體外/動物研究（PMID [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/)，European Journal of Haematology, 2007），直接確認 Fludarabine 對骨髓瘤細胞株（RPMI8226）具體外及體內抗腫瘤活性，並闡明 Akt 磷酸化抑制機轉，可支持此預測的生物學合理性。建議補充針對性文獻搜尋以完善證據鏈。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘌呤核苷類似物，Purine Nucleoside Analogue） |
| 骨髓抑制風險 | 高（嚴重嗜中性白血球減少、血小板減少、貧血為主要劑量限制毒性） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含白血球分類）、血小板、肝腎功能、電解質；長期使用需監測神經毒性及伺機性感染指標（CMV、EBV 再活化） |
| 處置防護 | 需依細胞毒性藥物處置規範操作；靜脈注射劑型調配時需穿戴適當防護裝備 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **已知重要安全性考量（來源：相關文獻及臨床試驗背景）**：Fludarabine 可造成嚴重免疫抑制，顯著增加機會性感染風險（包含 PCP、CMV/EBV 再活化）；高劑量時有神經毒性報告；可能誘發自體免疫性溶血性貧血；長期追蹤需留意治療相關 MDS/AML 發生風險（PMID [20962860](https://pubmed.ncbi.nlm.nih.gov/20962860/)）。骨髓瘤患者常伴腎功能不全，使用前須依腎功能調整劑量。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Fludarabine 在多發性骨髓瘤的異體移植前條件化及 CAR-T 淋巴清除應用已有多項 Phase 2 完成的臨床試驗支持（NCT01453101、NCT00802568 等），且體外研究（PMID 17976186）確認其對骨髓瘤細胞具直接抗腫瘤活性，同 B 細胞譜系腫瘤的機轉連結合理。然而香港目前無許可登記，且本次評估安全性仿單資料不完整，進一步推進需審慎設立管控措施。

**若要推進需要：**
- 補充完整作用機轉資料（MOA），特別是 Fludarabine 在漿細胞凋亡路徑中的詳細機制
- 取得原廠仿單完整安全性資訊（警語、禁忌症、藥物交互作用）
- 釐清目標應用定位：(1) 作為 allo-SCT/CAR-T 前處理（證據較充分）或 (2) 作為直接抗骨髓瘤藥物（需額外體內驗證）
- 在香港申請進口特許或啟動本地臨床試驗前須取得衛生署核准
- 補充針對性 PubMed 文獻搜尋，以完善漿細胞骨髓瘤的直接文獻證據鏈
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

