---
layout: default
title: Tenoxicam
parent: 高證據等級 (L1-L2)
nav_order: 731
evidence_level: L2
indication_count: 5
---

# Tenoxicam
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Tenoxicam：從關節/肌肉骨骼止痛消炎到類風濕性關節炎的再確證

## 一句話總結

Tenoxicam (DB00469) 是 oxicam 類 NSAID，目前**未在香港上市**，本地無任何許可證資料。
TxGNN 模型將**類風濕性關節炎 (Rheumatoid Arthritis)** 列為最高分預測適應症，
目前有 **1 個臨床試驗**和 **20 篇文獻**支持——但這實際上是該藥物在其他市場早已核准的**既有用途**，而非全新假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（香港未上市，無許可證資料可查） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Tenoxicam 是 oxicam 類非類固醇消炎止痛藥 (NSAID)，透過非選擇性抑制 COX-1/COX-2 降低前列腺素合成，達到消炎、鎮痛與解熱效果——這是 NSAID 類藥物治療類風濕性關節炎 (RA) 的標準藥理機轉。

需特別說明：本評估報告的結構化 MOA 欄位本身是資料缺口，但透過文獻與 TxGNN 推理路徑仍可還原其藥理邏輯。事實上，pack 中的推理備註明確指出——**RA 是 tenoxicam 已核准的既有適應症，而非新發現的再利用假說**，TxGNN 給出的高分反映的是模型正確捕捉到了真實已知的藥理關係，而非發掘出全新的機轉關聯。

文獻證據也支持此點：多篇 1985-1996 年的臨床研究（含至少 2 篇 RCT）顯示 tenoxicam 在 RA 治療上療效與 piroxicam、aceclofenac 等同類 NSAID 相當，安全性亦可比擬。這也解釋了為何此候選在證據強度上遠高於同批預測中的其他罕見症候群（如 brachydactyly-syndactyly syndrome），後者被判定為知識圖譜嵌入雜訊。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05508451](https://clinicaltrials.gov/study/NCT05508451) | NA | 完成 | 80 | 比較 tenoxicam 單方、paracetamol 單方及兩者合併於雙頜手術後疼痛之鎮痛效果，與關節疼痛適應症高度相關 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1593574](https://pubmed.ncbi.nlm.nih.gov/1593574/) | 1992 | RCT | J Rheumatol | 102 名 RA 患者比較 tenoxicam 20mg 與 piroxicam 20mg，療效無差異，安全性相當 |
| [8894360](https://pubmed.ncbi.nlm.nih.gov/8894360/) | 1996 | RCT | Clin Rheumatol | 292 名 RA 患者比較 aceclofenac 與 tenoxicam，兩組皆有臨床改善，完成率 81.1% |
| [1711963](https://pubmed.ncbi.nlm.nih.gov/1711963/) | 1991 | Review | Drugs | Tenoxicam 藥理與治療效益回顧：對 RA、OA、僵直性脊椎炎等風濕疾病療效與其他 NSAID 相當 |
| [8137596](https://pubmed.ncbi.nlm.nih.gov/8137596/) | 1994 | Review (PK) | Clin Pharmacokinet | Tenoxicam 臨床藥物動力學回顧，口服完全吸收，血漿蛋白結合率約 99% |
| [3915889](https://pubmed.ncbi.nlm.nih.gov/3915889/) | 1985 | Cohort/Open Trial | Eur J Rheumatol Inflamm | 79 名關節炎/RA 患者以肛門栓劑投予 tenoxicam 6 週，療效正向 |
| [3915885](https://pubmed.ncbi.nlm.nih.gov/3915885/) | 1985 | Cohort/Open Trial | Eur J Rheumatol Inflamm | 雙盲平行試驗顯示 tenoxicam 20mg 每日對 OA/RA/僵直性脊椎炎療效不亞於 piroxicam |
| [3262939](https://pubmed.ncbi.nlm.nih.gov/3262939/) | 1988 | PK Study | Ther Drug Monit | 單劑 40mg tenoxicam 於 RA/OA 患者血漿與滑液藥物動力學分析 |
| [8187453](https://pubmed.ncbi.nlm.nih.gov/8187453/) | 1994 | Mechanistic/Lab | Clin Rheumatol | Tenoxicam 對 RA 患者及健康對照組嗜中性球趨化性之影響研究 |
| [41419140](https://pubmed.ncbi.nlm.nih.gov/41419140/) | 2026 | Preclinical/Formulation | Eur J Pharm Sci | 開發 baricitinib+tenoxicam 共載奈米海綿凝膠，用於 RA 局部治療 |
| [2292331](https://pubmed.ncbi.nlm.nih.gov/2292331/) | 1990 | 多中心研究 | J Int Med Res | 2,963 名 OA/RA 患者於基層醫療環境接受 tenoxicam 20mg/日治療 12 週，症狀改善 |

---

## 其他預測適應症（補充參考）

本次評估共產生 5 個預測適應症，除首選 RA 外，其餘證據強度差異顯著：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|------|-----------|---------|------|
| 2 | Brachydactyly-syndactyly syndrome | 99.80% | L5 | Hold（先天骨骼發育症候群，與 NSAID 機轉無關聯，判定為模型雜訊） |
| 3 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.80% | L5 | Hold（同上，胚胎發育異常，無機轉關聯性） |
| 4 | Osteoarthritis susceptibility | 99.70% | L4 | Research Question（NSAID 類別層級證據充分，但無 tenoxicam 專屬試驗） |
| 5 | Headache disorder（急性偏頭痛） | 99.68% | L3 | Research Question（有 1 個 Phase 4 IV tenoxicam vs ibuprofen 試驗，尚未收案完成） |

---

## 安全性考量

> 安全性資訊請參考原廠仿單。目前缺乏 TFDA/HK 仿單警語、禁忌症及藥物交互作用資料（列為 Blocking 等級資料缺口），此項為進入 S1 安全性初評的必要前提。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- RA 適應症有 2 篇 RCT（tier 1）及多篇長期臨床觀察支持，證據等級達 L2，且此為國際間已知的既有適應症而非投機性假說，機轉合理性高。
- 但該藥物目前**未在香港上市**，無本地許可證與仿單資料，安全性初評（S1）所需的關鍵資訊（仿單警語、禁忌症）為 Blocking 缺口，尚無法進行完整風險評估。

**若要推進需要：**
- 取得 TFDA/香港衛生署仿單警語與禁忌症資料（DG001，Blocking，需下載仿單 PDF 解析）
- 補齊 DrugBank 結構化 MOA 資料（DG002，High）
- 若考慮香港市場准入，需啟動當地藥證申請流程並評估與現有 NSAID（如 piroxicam、diclofenac）的市場區隔
- 其餘 4 個預測適應症目前證據不足，暫不建議投入資源（Hold / Research Question）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

