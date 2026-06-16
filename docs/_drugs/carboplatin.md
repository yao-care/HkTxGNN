---
layout: default
title: Carboplatin
parent: 高證據等級 (L1-L2)
nav_order: 140
evidence_level: L1
indication_count: 10
---

# Carboplatin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Carboplatin：從卵巢癌（鉑類化療）到女性乳癌

## 一句話總結

Carboplatin 是第二代鉑類抗癌藥物，國際上廣泛用於卵巢癌、肺癌等多種實體腫瘤的一線化療，但目前未在香港衛生署登記上市。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效——尤其是三陰性乳癌（TNBC）及 HER2 陽性亞型，
目前有 **38 個臨床試驗**和 **20 篇文獻**支持這個方向，且已有多項 Phase 3 RCT 確認療效。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 卵巢癌等實體腫瘤（HK 無登記資料） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Carboplatin 屬第二代鉑類化療藥物，核心作用機轉為 **DNA 鏈間交聯**：鉑原子與 DNA 鳥嘌呤形成共價 Pt-adduct，阻斷 DNA 複製與轉錄，誘導腫瘤細胞凋亡。此機轉對分裂旺盛、DNA 修復功能受損的腫瘤細胞具選擇性毒性，是其廣泛應用於多種實體腫瘤的藥理基礎。

**三陰性乳癌（TNBC）**因缺乏 ER、PR、HER2 靶向途徑，對鉑類化療的敏感性較其他乳癌亞型更高。尤其是 **BRCA1/2 突變攜帶者**，因同源重組缺陷（HRD）導致 DNA 損傷修復功能喪失，對 Carboplatin 誘導的 DNA 交聯損傷尤為脆弱，療效顯著提升——此協同機制已由 BROCADE3（Phase 3 RCT）及多項 BRCA 特異性試驗驗證。

**HER2 陽性乳癌**方面，Carboplatin 與曲妥珠單抗（trastuzumab）聯用具有協同抗腫瘤效應。TCH 方案（docetaxel + carboplatin + trastuzumab）在 BCIRG 006 Phase 3 試驗（3,222 人）中與傳統含蒽環類方案療效相當，且心臟毒性顯著較低，已成為 HER2+ 早期乳癌輔助化療的重要選擇。GeparSixto（Phase 2 RCT，595 人）進一步確認加入 Carboplatin 可提升 TNBC 新輔助化療的病理完全緩解率（pCR），多項 2025 年 Phase 3 數據持續鞏固此方向。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | 完成 | 3,222 | BCIRG 006：比較 AC-T、AC-TH 與 TCH 方案輔助治療 HER2+ 早期乳癌，確立 Carboplatin + docetaxel + trastuzumab（TCH）的標準地位 |
| [NCT01426880](https://clinicaltrials.gov/study/NCT01426880) | Phase 2/3 | 完成 | 595 | 隨機評估 Carboplatin 加入 TNBC/HER2+ 新輔助化療方案（蒽環類 + taxane ± carboplatin）之療效，為直接相關規模最大試驗 |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | 完成 | 961 | GeparOcto：比較兩種劑量密集方案（ETC vs 含 carboplatin 的 PM(Cb)）用於高危早期乳癌新輔助治療 |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | 進行中（停止招募） | 720 | 隨機比較週 paclitaxel 加或不加 carboplatin 用於大型可切除或局部晚期 TNBC 新輔助治療 |
| [NCT01881230](https://clinicaltrials.gov/study/NCT01881230) | Phase 2/3 | 完成 | 191 | 比較 nab-paclitaxel + gemcitabine 或 carboplatin 與 gemcitabine/carboplatin 作為三陰性轉移性乳癌（TNMBC）一線治療 |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | 完成 | 45 | NEAT 試驗：bevacizumab + docetaxel + carboplatin 新輔助治療 TNBC，直接評估 Carboplatin 在 TNBC 中的療效與安全性 |
| [NCT03639948](https://clinicaltrials.gov/study/NCT03639948) | Phase 2 | 進行中（停止招募） | 120 | pembrolizumab + carboplatin + docetaxel 新輔助治療 Stage I-III TNBC，探索免疫聯合化療的協同效益 |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | 完成 | 148 | BRCA 試驗：隨機比較 carboplatin 與 docetaxel 用於 BRCA 突變轉移性遺傳性乳癌，直接評估鉑類亞族特異性療效 |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | 完成 | 103 | Olaparib（PARP 抑制劑）+ carboplatin 用於 BRCA1/2 突變乳癌及卵巢癌，確認 HRD 協同機制及最佳劑量 |
| [NCT07074106](https://clinicaltrials.gov/study/NCT07074106) | Phase 2 | 尚未招募 | 40 | DespaTIL：以 TIL 指數及影像反應引導的早期 TNBC 降階新輔助化療，評估輕量化 carboplatin 方案可行性 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | Phase 2 RCT | Lancet Oncology | GeparSixto：Carboplatin 加入新輔助化療方案，TNBC 的 pCR 率從 36.9% 顯著提升至 53.2% |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | Randomized Phase 2 | Clin Cancer Res | NeoSTOP：含蒽環類與無蒽環類的兩種 Carboplatin 新輔助方案在 Stage I-III TNBC 的 pCR 率相當，無蒽環方案毒性更低 |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | Phase 3 RCT | JAMA | CamRelief：Camrelizumab（抗 PD-1）+ 含鉑類 4 藥方案顯著改善早期/局部晚期 TNBC 新輔助病理完全緩解率 |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | Phase 3 RCT | Nature Communications | MUKDEN 06：ARX788（ADC）+ pyrotinib 與標準 TCbHP（含 carboplatin）隨機比較，直接確認 carboplatin 方案作為 HER2+ 新輔助對照基準 |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | Phase 3 RCT | Eur J Cancer | BROCADE3 最終 OS 數據：Veliparib + carboplatin/paclitaxel 在 BRCA 突變 HER2 陰性晚期乳癌中顯著改善 PFS，OS 有正向趨勢 |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Systematic Review | Med Oncol | Paclitaxel-carboplatin 聯合用於晚期乳癌的協同效應、療效及安全性系統回顧，奠定組合的藥理基礎 |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-analysis | PLoS One | 統合分析確認 carboplatin（及 bevacizumab）加入新輔助化療均可顯著提升 TNBC 的 pCR 率 |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | Randomized Phase 2 | Breast Cancer Res Treat | 隨機比較 carboplatin 單藥與 carboplatin + everolimus 用於晚期 TNBC，評估 mTOR 路徑活化對鉑類療效的調節作用 |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 | Breast Cancer Res | Bevacizumab + carboplatin 治療乳癌腦轉移的安全性與療效，提供特殊轉移部位的用藥依據 |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase 2 | Breast Cancer Res Treat | Carboplatin + gemcitabine + mifepristone（GR 拮抗劑）：探索糖皮質激素受體拮抗增強鉑類細胞毒性的新機轉及初步療效 |

---

## 香港上市資訊

Carboplatin 目前**未在香港衛生署登記上市**，無有效藥品許可證記錄。如需於香港臨床使用，須透過「未經登記藥劑製品特別申請」途徑（Special Patient Application / Import Licence）向衛生署辦理進口許可。

---

## 細胞毒性

Carboplatin 屬傳統鉑類細胞毒性化療藥物，用於乳癌治療時需特別留意下列安全事項：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Platinum compound，DNA 鏈間交聯劑） |
| 骨髓抑制風險 | **高**（主要劑量限制性毒性：**血小板減少症**為 Carboplatin 特徵性毒性，嗜中性白血球減少亦常見，尤其於聯合化療方案中更為顯著） |
| 致吐性分級 | 中至高度致吐性（依劑量 AUC 及聯合方案而異，標準 AUC 5-6 屬中度致吐） |
| 監測項目 | CBC 含分類（特別是血小板計數、ANC）、血清肌酐及腎功能（eGFR，用於 Calvert 公式 AUC 劑量計算）、電解質（鎂、鈣）、聽力（高劑量方案） |
| 處置防護 | 需依細胞毒性藥物處置規範操作（密閉系統轉注、生物安全櫃、個人防護裝備）；腎功能不全者必須依 Calvert 公式調整劑量，GFR < 15 mL/min 禁用 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Carboplatin 用於女性乳癌（尤其 TNBC 及 HER2+ 亞型）具備充分的 L1 級臨床證據，包含多項已完成的 Phase 2/3 RCT（GeparSixto、GeparOcto、BCIRG 006）及 BROCADE3（Phase 3）等大型試驗。Carboplatin 加入 paclitaxel / docetaxel ± trastuzumab 的新輔助及輔助化療方案已被多個國際腫瘤學指引採納，是 TNBC 及 HER2+ 乳癌的重要治療選項，TxGNN 預測（99.86%）高度吻合現有臨床實證。

**若要推進需要：**
- 向香港衛生署申請 Carboplatin 進口特別許可（目前未登記）
- 補充完整香港/台灣仿單安全性資料（警語、禁忌症），目前資料缺口（DG001）為 Blocking 等級
- 明確目標族群（TNBC vs HER2+ vs BRCA 突變者），並制定相應的生物標記篩選策略（如 HRD 評分、PD-L1 CPS）
- 依患者腎功能（eGFR）以 Calvert 公式精確計算每療程 Carboplatin AUC 給藥劑量
- 評估與免疫檢查點抑制劑（pembrolizumab、camrelizumab）聯合使用的可行性，呼應 2025 年多項 Phase 3 趨勢
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

