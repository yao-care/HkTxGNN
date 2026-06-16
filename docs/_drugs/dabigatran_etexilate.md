---
layout: default
title: Dabigatran Etexilate
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 5
---

# Dabigatran Etexilate
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

# Dabigatran Etexilate：從抗凝血治療到硬化性膽管炎

## 一句話總結

Dabigatran Etexilate（Pradaxa®）是一種直接口服凝血酶抑制劑，全球廣泛用於心房顫動患者的腦中風預防及靜脈血栓栓塞症的治療與預防，但目前香港尚未上市。TxGNN 模型在本批次預測 5 個新適應症，首要預測為**硬化性膽管炎 (Sclerosing Cholangitis)**，TxGNN 分數高達 99.82%，然而目前**無直接臨床試驗**、僅有 **1 篇間接文獻**，整體證據極為初步；批次中機轉連結最合理的適應症反而是排名第 5 的血小板原發性釋放功能障礙，具相對較多間接支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心房顫動腦中風預防、靜脈血栓栓塞症治療與預防（全球核准；香港未上市） |
| 預測新適應症（排名 #1） | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Dabigatran Etexilate 在香港藥監系統的詳細作用機轉登錄資料。根據國際文獻，Dabigatran Etexilate 是 dabigatran 的前驅藥（prodrug），口服後在體內轉化為活性型 dabigatran，直接且可逆地抑制凝血酶（thrombin, Factor IIa），阻斷纖維蛋白原轉化為纖維蛋白，達到抗凝血效果。

就機轉推論而言，Thrombin 可透過 PAR-1/PAR-2 受體活化肝星狀細胞（hepatic stellate cells），促進 TGF-β 分泌，進而加速膽管周圍纖維化。在原發性硬化性膽管炎（PSC）患者中，亦有觀察性報告指出凝血系統異常活化的現象。因此理論上，抑制 thrombin 可能緩解膽管炎性纖維化進程，為 TxGNN 預測提供了初步的生物學合理性。

然而，上述假說目前仍停留在動物模型及間接推論層次，**尚無任何以 Dabigatran 治療硬化性膽管炎的臨床前或臨床研究資料**，機轉假說的臨床可行性有待驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | DDI 藥動學研究 | Clinical Pharmacokinetics | 探討 Cilofexor（FXR 促效劑，正用於 PSC 開發中）的藥物交互作用潛力；未涉及 Dabigatran 的直接療效 |

> ⚠️ 上述文獻研究的主角為另一種藥物（cilofexor），僅間接確認 PSC 治療研究的背景脈絡，**並非 Dabigatran 在硬化性膽管炎中療效的直接證據**。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 附：本批次全部預測適應症概覽

本批次共預測 5 個適應症，整體概況如下：

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議 | 機轉評析 |
|------|--------|-----------|---------|------|---------|
| 1 | 硬化性膽管炎 | 99.82% | L5 | Research Question | thrombin-肝纖維化路徑具假說合理性，但零直接證據 |
| 2 | 家族性混合型高脂血症（廢棄分類）| 99.63% | L5 | Hold | 機轉無關；疾病分類本體論已廢棄 |
| 3 | 低 α-脂蛋白血症 | 99.57% | L5 | Hold | 機轉無關（ABCA1/HDL 路徑與凝血無直接關聯） |
| 4 | 同型合子家族性高膽固醇血症 | 99.49% | L5 | Hold | 機轉無關（LDL 受體缺損路徑）；疑 KG 系統性誤連結 |
| 5 | 血小板原發性釋放功能障礙 | 99.06% | L4 | Research Question | 機轉連結最為直接；有間接臨床及文獻支持 |

> ⚠️ **知識圖譜品質警示**：本批次排名 2、3、4 的三個脂質相關適應症同時具有極高 TxGNN 分數，但均為零證據支持，且 Dabigatran 的凝血酶抑制機轉與脂質代謝路徑無已知直接關聯，**強烈建議審查知識圖譜中脂質疾病節點是否存在系統性誤連結**。

---

### 重點補充：排名第 5 — 血小板原發性釋放功能障礙

**機轉連結（為何最合理）**：Dabigatran 抑制 thrombin，而 thrombin 正是透過 PAR-1/PAR-4 觸發血小板脫顆粒（granule release）的最強生理性活化劑之一。在 delta storage pool disease、gray platelet syndrome 等血小板釋放功能障礙中，凝血瀑布異常活化可能加重出血或引發矛盾性血栓（如 HIT 機轉）。理論上抑制 thrombin 可減少其介導的血小板二次活化信號，具一定治療合理性。⚠️ 然而需注意：若患者本身已有血小板功能低下，額外抗凝可能大幅提升出血風險，需審慎評估獲益風險比。

#### 臨床試驗（間接相關，C 級相關性）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06101667](https://clinicaltrials.gov/study/NCT06101667) | NA | 招募中 | 224 | 急性基底動脈閉塞血管內再通治療 vs 藥物管理（ANGEL-BAO）；與血小板釋放功能障礙無直接關聯，Dabigatran 僅可能作為背景抗凝用藥 |

#### 文獻（間接相關）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28646118](https://pubmed.ncbi.nlm.nih.gov/28646118/) | 2017 | 回顧性研究＋文獻回顧 | Blood | DOACs 用於 HIT（肝素誘發性血小板減少症）治療；以 rivaroxaban 為主，間接涉及 thrombin 抑制與血小板異常的關係 |
| [31505555](https://pubmed.ncbi.nlm.nih.gov/31505555/) | 2019 | 回顧／指引分析 | AJHP | 心房顫動合併冠狀動脈支架置入術患者的抗血栓組合療法更新指引 |
| [39133737](https://pubmed.ncbi.nlm.nih.gov/39133737/) | 2024 | 橫斷面調查 | Pain Physician | 介入性疼痛處置的抗血小板／抗凝劑圍手術期管理實務模式調查 |
| [19875000](https://pubmed.ncbi.nlm.nih.gov/19875000/) | 2009 | Review | Ann Fr Anesth Réanim | Dabigatran（Pradaxa）療效與安全性綜述，聚焦原適應症血栓預防 |

---

## 結論與下一步

**決策：Hold**

**理由：**
首要預測適應症（硬化性膽管炎）雖具 thrombin-纖維化軸的機轉假說，但完全缺乏直接臨床前或臨床證據（L5），加之香港未上市需額外投入市場準入資源，目前不建議推進。批次中 3 個脂質適應症的高分預測高度疑似圖譜誤連結，不具臨床追蹤價值。血小板釋放功能障礙（排名 5）雖為本批次機轉最合理的預測，但文獻均屬間接相關，且此適應症使用抗凝劑存在顯著出血安全疑慮，需更多基礎研究支持。

**若要推進需要：**
- 確認 Dabigatran Etexilate 在香港的上市路徑（補件或重新注冊），評估市場準入可行性
- 補充正式 MOA 資料（向 DrugBank API 查詢 DB06695）及 TFDA 仿單警語與禁忌資料
- 針對硬化性膽管炎方向，系統搜尋 dabigatran 或其他直接 thrombin 抑制劑的肝纖維化、PSC 動物模型研究
- 審查 TxGNN 知識圖譜中脂質疾病節點（FH、hypoalphalipoproteinemia、mixed hyperlipidemia）的連結品質，確認是否存在系統性誤連結並修正
- 若考慮推進血小板釋放功能障礙方向，需先完成出血風險-獲益比分析，並尋求血液科專家意見後再設計前臨床實驗
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

