---
layout: default
title: Captopril
parent: 中證據等級 (L3-L4)
nav_order: 135
evidence_level: L3
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L3** | 預測適應症: **4** 個
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

# Captopril：從高血壓到惡性腎血管性高血壓

## 一句話總結

Captopril 是第一個上市的口服 ACE 抑制劑（ACEi），原本用於高血壓及心臟衰竭的治療。TxGNN 模型預測它可能對**惡性腎血管性高血壓（Malignant Renovascular Hypertension）** 有效，目前有 **0 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（ACEi 一線藥物；仿單資料待補充） |
| 預測新適應症 | 惡性腎血管性高血壓（Malignant Renovascular Hypertension） |
| TxGNN 預測分數 | 99.28% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

> **選取依據說明**：TxGNN 共預測 4 個適應症，前兩項分數相同（99.28%）。本報告以**惡性腎血管性高血壓（rank 2）** 為主要討論對象，因其文獻支持較充分（20 篇 vs 1 篇）且建議等級較高（Proceed with Guardrails vs Hold）。

---

## 為什麼這個預測合理？

Captopril 是 ACE 抑制劑（Angiotensin-Converting Enzyme Inhibitor）的先驅藥物，透過競爭性阻斷 ACE，抑制 Angiotensin I 轉化為 Angiotensin II（Ang II），從而降低周邊血管阻力、抑制醛固酮分泌，達到降壓及減少水鈉滯留的效果。

腎血管性高血壓的核心病理鏈為：腎動脈狹窄（RAS）→ 腎臟缺血 → 腎素大量釋放 → RAAS 過度活化 → Ang II 驅動血壓持續上升。惡性期定義為血壓 >180/120 mmHg 並伴隨視乳頭水腫或終器官損傷。Captopril 直接截斷 Ang II 的生成，是此病態最精準的藥理介入點，機轉合理性高。文獻記載 Captopril 在腎素依賴性高血壓患者中可使血壓顯著下降，並可誘導血漿腎素活性（PRA）顯著上升，已被用作腎血管性高血壓的診斷性激發試驗。

**關鍵安全考量**：若惡性腎血管性高血壓伴隨**雙側腎動脈狹窄**，移除 Ang II 對出球小動脈的代償性收縮後，腎小球過濾壓可能驟降，有誘發急性腎功能惡化的風險。此為使用 ACEi 前必須排除的臨床禁忌，需影像學確認腎動脈通暢性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

### 惡性腎血管性高血壓（Rank 2，20 篇）

共 20 篇相關文獻，依相關性列出前 10 篇：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | 臨床觀察 | Biull Vsesoiuz Kardiol | Captopril 用於穩定期及惡性高血壓患者的療效觀察 |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | 臨床研究 | Clin Science | Captopril 誘導 PRA 升高用於鑑別腎血管性高血壓，44/44 患者達陽性閾值 |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | J Pediatrics | 兒童惡性高血壓的病理生理與治療概覽 |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Medica | 腎血管性高血壓臨床概念：RAAS 阻斷為核心治療策略 |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review/Case Series | Endocrinol Metab Clin NA | 腎素分泌腫瘤：Captopril 給藥後血壓顯著下降，確認腎素依賴性 |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case Report + Review | Clinical Nephrology | NF1 合併腎血管性高血壓 2 例，Captopril 激發試驗確認 RAAS 過度活化 |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Case Series | Pediatric Nephrology | 27 名 NF1 兒童接受 Captopril 試驗評估腎血管性病變及繼發性高血壓 |
| [3928961](https://pubmed.ncbi.nlm.nih.gov/3928961/) | 1985 | Case Report | Klin Wochenschr | 腹主動脈縮窄合併雙側腎動脈狹窄，Captopril 長期控制嚴重腎血管性高血壓 |
| [1436350](https://pubmed.ncbi.nlm.nih.gov/1436350/) | 1992 | Case Report | Nephron | VHL 病合併嗜鉻細胞瘤致高腎素血症，Captopril 使血壓改善，腎素分泌進一步上升 |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case Report | Clin Nuclear Med | 惡性高血壓患者 Captopril 腎閃爍圖偽陽性，腎動脈無狹窄但腎功能代償異常 |

### 惡性高血壓性腎病（Rank 1，1 篇）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case Report | Clin Nuclear Med | Captopril 腎圖陽性但無腎動脈狹窄，發現腎細胞癌致腎素依賴性高血壓，腎切除後血壓恢復正常 |

---

## 預測適應症一覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|--------|-----------|---------|------|
| 1 | 惡性高血壓性腎病（Malignant Hypertensive Renal Disease） | 99.28% | L4 | Hold |
| 2 | 惡性腎血管性高血壓（Malignant Renovascular Hypertension） | 99.28% | L3 | **Proceed with Guardrails** |
| 3 | 機轉不明肺動脈高壓（PH with Unclear Multifactorial Mechanism） | 99.15% | L5 | Hold |
| 4 | 肺病或低氧引發之肺動脈高壓（PH due to Lung Disease/Hypoxia） | 99.15% | L5 | Hold |

> **Rank 3 & 4 說明**：肺動脈高壓的標準治療以 ERA（Bosentan）、PDE5i（Sildenafil）、前列環素類為主，ACEi 療效未獲確立。文獻中找到的 20 篇「低氧相關」文獻與 Captopril 無直接關聯（均為低氧病理機轉研究），不支持推進。

---

## 香港上市資訊

Captopril 目前在香港**未上市**，無任何許可證紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **機轉特異性安全警示**：使用 ACEi 治療腎血管性高血壓前，須影像學排除雙側腎動脈狹窄（bilateral RAS）。雙側 RAS 患者使用 ACEi 後，因出球小動脈代償性收縮消失，可能引發急性腎功能惡化（GFR 驟降），為此適應症使用的首要安全把關項目。

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對惡性腎血管性高血壓）

**理由：**
Captopril 的 ACEi 機轉直接對應腎血管性高血壓的 RAAS 過度活化病理，文獻中有臨床觀察及多篇案例研究記錄其在腎素依賴性高血壓中的確實療效，機轉合理性強、文獻支持達 L3 等級。但雙側 RAS 禁忌及仿單資料缺口為推進前的關鍵障礙。

**若要推進需要：**
- 補充香港 / TFDA 仿單安全警語與禁忌症（DG001，Blocking 級）
- 補充正式 MOA 文獻引用（DG002，High 級）
- 使用前影像學確認腎動脈通暢性（排除雙側 RAS，避免急性腎損傷）
- 評估香港上市申請可行性（目前零許可證，需從頭申請）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

