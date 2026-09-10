---
layout: default
title: Iron
parent: 中證據等級 (L3-L4)
nav_order: 413
evidence_level: L3
indication_count: 5
---

# Iron
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Iron：從缺鐵性貧血到 Plummer-Vinson 症候群

## 一句話總結

Iron（DrugBank DB01592）為治療缺鐵性貧血的基礎礦物質補充劑。本次 TxGNN 對其產生 5 個預測適應症，其中證據品質最高、機轉最直接的是 **Plummer-Vinson 症候群**——此症的核心病理本身就是慢性缺鐵性貧血，目前有 **19 篇文獻**支持鐵劑補充為其常規治療的一環；其餘 4 個預測則缺乏機轉支持或僅為間接關聯，建議暫緩（Hold）。

> 註：本 Evidence Pack 含多個候選適應症（candidate_id 標示為 multi），以下報告以證據等級最高、決策階段最進階的候選為主軸，其餘候選於「候選總覽」中列出並說明擱置原因。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 缺鐵性貧血（Iron Deficiency Anemia，屬鐵劑之公認核心用途；本 Evidence Pack 未收錄正式核准適應症文字與 MOA，列為資料缺口） |
| 預測新適應症 | Plummer-Vinson 症候群（Plummer-Vinson Syndrome） |
| TxGNN 預測分數 | 99.89%（rank 2857） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 候選總覽

TxGNN 針對 IRON 共產生 5 個預測適應症，證據強度與建議差異很大：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 備註 |
|------|-----------|-----------|---------|------|------|
| 1 | Vitamin B12/folate-independent 先天性巨球性貧血 | 99.89% | L5 | Hold | 病理機轉與鐵缺乏方向相反，無文獻/試驗支持，判定為圖譜鄰近性假陽性 |
| 2 | **Plummer-Vinson 症候群** | 99.89% | L3 | **Proceed with Guardrails** | 缺鐵性貧血為其核心病理，鐵劑補充機轉直接 |
| 3 | 非症候群性食道畸形 | 99.86% | L5 | Hold | 構造性畸形非鐵缺乏可解釋，無任何證據 |
| 4 | 生物素代謝疾病 | 99.74% | L4 | Hold | 僅有間接的粒線體輔因子理論關聯，無直接介入研究 |
| 5 | 維生素缺乏症（廣義） | 99.68% | L3 | Research Question | 語意過於寬泛，多數證據為共同補充研究而非以鐵治療該病 |

以下章節聚焦於證據最充分的候選：**Plummer-Vinson 症候群**。

---

## 為什麼這個預測合理？

本 Evidence Pack 未收錄 IRON 的正式 DrugBank MOA 敘述與台灣/香港核准適應症文字（列為資料缺口 DG002）。根據已知藥理學與本次蒐集之文獻，鐵劑的核心用途是治療缺鐵性貧血。

Plummer-Vinson 症候群（又稱 Paterson-Kelly / Paterson-Brown-Kelly 症候群）的典型三聯症就是**吞嚥困難、缺鐵性貧血、食道蹼**。多篇文獻（如 PMID 12823219、7575056）明確指出鐵劑補充是治療此症貧血成分的一線方法，部分病例甚至因鐵劑補充而使吞嚥困難獲得改善。

因此，這並非典型的「老藥新用」機轉外推，而是機轉上直接對應：鐵劑治療的是該症候群病理三聯症中的貧血組成部分，屬於既有臨床實務中已被驗證的關聯，而非全新假說。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29089792](https://pubmed.ncbi.nlm.nih.gov/29089792/) | 2017 | Review | Journal of Blood Medicine | 回顧缺鐵性貧血與 Plummer-Vinson 症候群的關聯與現況 |
| [16978405](https://pubmed.ncbi.nlm.nih.gov/16978405/) | 2006 | Review | Orphanet Journal of Rare Diseases | 經典三聯症（吞嚥困難、缺鐵性貧血、食道蹼）綜述，好發於中年白人女性 |
| [12823219](https://pubmed.ncbi.nlm.nih.gov/12823219/) | 2003 | Review/病例報告 | Diseases of the Esophagus | 2 例個案經鐵劑補充後症狀（吞嚥困難、舌炎、口角炎）消失 |
| [7865729](https://pubmed.ncbi.nlm.nih.gov/7865729/) | 1994 | Review | J Gastroenterol Hepatol | 探討本病發生率下降的三種假說，含缺鐵為主要病因之一 |
| [20890819](https://pubmed.ncbi.nlm.nih.gov/20890819/) | 2010 | Review | La Tunisie Médicale | 好發於白人女性之罕見缺鐵性貧血合併食道蹼病症綜述 |
| [34651287](https://pubmed.ncbi.nlm.nih.gov/34651287/) | 2022 | Case-based Review | Immunologic Research | Sjögren 症候群病人併發 Plummer-Vinson 症候群之系統性文獻回顧 |
| [31208220](https://pubmed.ncbi.nlm.nih.gov/31208220/) | 2019 | Review | Ear, Nose & Throat Journal | 病症概述 |
| [38871147](https://pubmed.ncbi.nlm.nih.gov/38871147/) | 2024 | Review | Clin Gastroenterol Hepatol | 缺鐵性貧血、吞嚥困難、食道蹼經典三聯症之影像/內視鏡呈現 |
| [38034443](https://pubmed.ncbi.nlm.nih.gov/38034443/) | 2023 | Case Report | JPGN Reports | 4 歲兒童個案，經內視鏡氣球擴張術合併鐵缺乏處置 |
| [41756818](https://pubmed.ncbi.nlm.nih.gov/41756818/) | 2026 | Case Report | Case Reports in Hematology | 26 歲女性長期吞嚥困難合併缺鐵性貧血個案 |

（另有 8 篇分類待補之相關文獻，因篇幅限制未列出）

---

## 香港上市資訊

Iron（DB01592）目前在香港**未上市**，無許可證登記資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（本 Evidence Pack 之 TFDA 仿單警語/禁忌資料缺口列為 Blocking 等級，於進入正式安全性初評 S1 前須先補齊。）

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅適用於 Plummer-Vinson 症候群此一候選；其餘 4 個候選維持 Hold）

**理由：**
- Plummer-Vinson 症候群之病理核心即為缺鐵性貧血，鐵劑補充機轉直接且有 19 篇文獻（多為 Review/個案報告）佐證，屬於既有臨床實務範疇的延伸確認，而非高風險新假說。
- 其餘候選（先天性巨球性貧血、食道畸形、生物素代謝疾病、廣義維生素缺乏症）機轉方向不符或證據不足，暫不推進。

**若要推進需要：**
- 補齊 TFDA/香港藥品仿單警語與禁忌資料（DG001，Blocking，須先完成才能進入 S1 安全性初評）
- 補齊 DrugBank MOA 與正式核准適應症文字（DG002）
- 因目前無 RCT/介入性臨床試驗直接驗證「以鐵劑治療 Plummer-Vinson 症候群」，若要提升至 L1/L2 證據等級，需規劃前瞻性介入研究或系統性回顧
- 確認香港上市/引進路徑（目前 total_licenses = 0）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

