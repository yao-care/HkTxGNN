---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dasatinib：預測新適應症為尤文氏肉瘤 (Ewing sarcoma)（證據等級 L5）。原適應症：慢性骨髓性白血病（BCR-ABL1 陽性）、慢性骨髓性白血病急性母細胞期"
monitor_inn: "DASATINIB"
predicted_indications: ["Ewing sarcoma", "liposarcoma", "fibromatosis, gingival", "dermatofibrosarcoma protuberans", "ovarian myxoid liposarcoma", "ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung"]
---

# Dasatinib
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

# Dasatinib：從慢性骨髓性白血病到尤文氏肉瘤

## 一句話總結

Dasatinib 是一種口服多標靶酪胺酸激酶抑制劑，原本用於 BCR-ABL1 陽性的慢性骨髓性白血病（含急性母細胞期）。
TxGNN 模型預測它可能對**尤文氏肉瘤 (Ewing sarcoma)** 有效，目前有 **2 個臨床試驗**和 **10 篇文獻**與此方向相關。但證據以前臨床研究為主，已有的 2 期試驗顯示單藥在此亞型並未成功。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性骨髓性白血病（BCR-ABL1 陽性）、慢性骨髓性白血病急性母細胞期 |
| 預測新適應症 | 尤文氏肉瘤 (Ewing sarcoma) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L2（依資料彙整的評等；但該等級主要來自一項非尤文氏肉瘤專屬的 2 期試驗，實際證據偏弱，詳見下文） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（列為研究性問題） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠 MOA 欄位未收錄）。不過依文獻，dasatinib 是 BCR-ABL 與 SRC 家族激酶的抑制劑，同時也抑制 KIT 與 PDGFR。

尤文氏肉瘤是好發於青少年與年輕成人的骨與軟組織腫瘤。多項前臨床研究顯示，Src/FAK 訊號參與尤文氏肉瘤細胞的侵襲、遷移與 invadopodia 形成（PMID 18202781、27566104、31521948、35655525）。因此，以 SRC 抑制劑阻斷這條路徑在機轉上說得通。

但要注意：一項針對晚期肉瘤的 2 期研究顯示，dasatinib 單藥在尤文氏肉瘤與橫紋肌肉瘤亞型**未能成功**（見 PMID 35655525 的回顧）。因此較合理的方向是合併療法，而非單藥。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | 已終止 | 7 | 兒童病人使用 dasatinib 合併 ifosfamide、carboplatin、etoposide；僅收 7 人即終止，提供的安全性或療效資訊極少 |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | 完成 | 366 | dasatinib 單藥用於晚期肉瘤，評估反應率與 6 個月無惡化存活率；非尤文氏肉瘤專屬，未提供亞型層級的結果 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [42804591](https://pubmed.ncbi.nlm.nih.gov/42804591/) | 2026 | 描述性病例系列 | J Pediatr Hematol Oncol | 以 RIST 方案（rapamycin、irinotecan、dasatinib、temozolomide）治療復發性尤文氏肉瘤的單中心經驗 |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Review | Sarcoma | 探討 FAK-Src 複合體作為標靶；指出 dasatinib 單藥在尤文氏肉瘤與橫紋肌肉瘤的 2 期研究中失敗 |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncol Lett | Src 訊號在肉瘤中的角色，並討論其作為藥物標靶的可行性 |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | 前臨床（體外） | Oncol Rep | dasatinib 抑制神經母細胞瘤與尤文氏肉瘤細胞株的增殖與遷移 |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | 前臨床（體外） | Cancer Res | dasatinib 抑制多種肉瘤細胞株的遷移與侵襲，並誘導依賴 SRC 的骨肉瘤細胞凋亡 |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | 前臨床（體外） | Neoplasia | 微環境壓力透過 Src 促進尤文氏肉瘤的侵襲與細胞遷移 |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | 前臨床（體外） | Neoplasia | Tenascin C 與 Src 協同促進尤文氏肉瘤 invadopodia 形成 |

---

## 香港上市資訊

香港共有 20 張有效的單一成分 dasatinib 許可證，無已註銷者。以下列出 5 張主要許可證（資料中未收錄劑型與核准適應症文字）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55803 | SPRYCEL TAB 70MG | Bristol-Myers Squibb Pharma (HK) Ltd |
| HK-55804 | SPRYCEL TAB 50MG | Bristol-Myers Squibb Pharma (HK) Ltd |
| HK-55805 | SPRYCEL TAB 20MG | Bristol-Myers Squibb Pharma (HK) Ltd |
| HK-66653 | DASATINIB SANDOZ TABLETS 20MG | Sandoz Hong Kong Limited |
| HK-67501 | DASATINIB TEVA TABLETS 20MG | Teva Pharmaceutical Hong Kong Limited |

其餘許可證包括 Apo-Dasatinib（Hind Wing）、Stada、Teva、Sandoz、Scigen（DCH Auriga）與 Jindun 的學名藥，規格涵蓋 20 mg、50 mg、70 mg。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 資料中未提供詳細數據；知識圖譜顯示血小板減少、嗜中性白血球減少、顆粒球缺乏症、貧血為列入禁忌的相關疾病，需特別留意 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 建議監測全血球計數（CBC）、肝功能、心電圖（QT 間期）與體液滯留徵象 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自藥物與疾病關聯資料，非仿單原文）：長 QT 症候群（含家族性）、尖端扭轉型心室頻脈、肝病、膽囊疾病、血小板減少、嗜中性白血球減少、顆粒球缺乏症、貧血、充血性心衰竭、心肌梗塞、冠狀動脈血栓、血色素病變、活動性消化性潰瘍、腦內出血、心包積液。
- **藥物交互作用**：共查得 100 筆，以下為主要項目。
  - **重大 (Major)**：famotidine、ranitidine、cimetidine、rabeprazole、omeprazole（降低胃酸的藥物可能降低 dasatinib 吸收）；dexamethasone；acetylsalicylic acid；clarithromycin
  - **中度 (Moderate)**：hydrocortisone、budesonide、loperamide、aprepitant、bisacodyl、magnesium oxide、aluminum hydroxide、calcium carbonate、saxagliptin 等

香港仿單的警語與禁忌尚未取得，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（列為研究性問題）**

**理由：**
- 尤文氏肉瘤的證據主要為前臨床研究，唯一的肉瘤 2 期試驗並非尤文氏專屬，且文獻指出單藥在此亞型失敗。TxGNN 分數很高（99.90%），但不足以支持臨床推進。
- 排名第 2 的「骨髓性白血病」雖有 L1 證據（如 DASISION 的 3 期試驗），但這與原適應症重疊，並非真正的新用途。真正新穎的方向是 KIT 驅動疾病，如核心結合因子急性骨髓性白血病（CBF-AML）的 3 期研究（PMID 41490515）。

**若要推進需要：**
- 取得 RIST 等合併方案的前瞻性臨床數據，並確認尤文氏肉瘤亞型的療效
- 取得 dasatinib 的作用機轉資料與香港仿單的警語與禁忌
- 針對心血管（QT 延長、心衰竭、心包積液）與血液學風險擬定監測計畫，特別是兒童與青年族群
- 評估與抑酸劑、CYP3A4 抑制劑等重大交互作用的管理方式
- 若想尋找更有利的新適應症，可另行評估 CBF-AML（KIT 突變）方向
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

