---
layout: default
title: Oxymetazoline
parent: 中證據等級 (L3-L4)
nav_order: 639
evidence_level: L3
indication_count: 3
---

# Oxymetazoline
{: .fs-9 }

證據等級: **L3** | 預測適應症: **3** 個
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

# Oxymetazoline：從鼻減充血劑到鼻腔疾病

## 一句話總結

Oxymetazoline 是局部使用的 α-腎上腺素受體促效劑，在香港以鼻用製劑上市，用於鼻塞的減充血。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效。
目前有 **17 個臨床試驗**和 **5 篇文獻**與此方向相關，但其中多數是間接證據，且這個預測更接近既有用途，不算真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 局部鼻減充血（許可證資料未載明適應症文字，此為依藥理類別的判斷） |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。Oxymetazoline 屬於局部使用的 α-腎上腺素受體促效劑。它使鼻黏膜血管收縮，降低黏膜腫脹，改善鼻腔通氣。

這個機轉與鼻腔疾病（以鼻塞、黏膜充血為主要表現）在生物學上相符。它與藥物本身既有的鼻減充血用途高度重疊，所以預測較接近「符合現有用途」，而不是全新的適應症。

TxGNN 的高分（99.96%）很可能反映這種已知的藥物類別與疾病關聯。原適應症欄位為空、MOA 缺漏，比較像資料不完整，並非新用途的訊號。這裡的證據強度相當於一個已上市的減充血劑，不能視為強力的新用途證據。

---

## 臨床試驗證據

以下列出 10 個相對相關的試驗。多數是「鼻腔處置或評估」情境，不是以 oxymetazoline 治療疾病為主要終點。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | 完成 | 20 | 比較 0.05% oxymetazoline 與 1:1000 epinephrine 在鼻竇內視鏡手術前使用的出血量與術野可見度 |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | 完成 | 160 | 雙盲隨機試驗，比較局部麻醉或減充血劑預處理對纖維鼻咽喉鏡檢查疼痛與不適的影響，支持鼻腔處置用途，並非治療疾病 |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | NA | 完成 | 106 | 比較 Co-phenylcaine（減充血加局部麻醉）鼻噴霧與鼻霧化，用於硬式鼻內視鏡檢查前 |
| [NCT01411969](https://clinicaltrials.gov/study/NCT01411969) | NA | 完成 | 16 | 以 0.05% oxymetazoline 噴霧減充血後，用聲學鼻量測法評估外用鼻擴張貼片對鼻腔波形的影響 |
| [NCT00147940](https://clinicaltrials.gov/study/NCT00147940) | Phase 4 | 終止 | 20 | 以聲學鼻量測法與鼻音計檢視鼻腔容積與鼻音度的相關性，樣本小且已終止，證據薄弱 |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | 完成 | 21 | 隨機、雙盲、安慰劑對照的四向交叉試驗，在季節性過敏性鼻炎患者中評估 H3 受體拮抗劑對鼻過敏原激發後鼻塞的影響。試驗藥物與終點尚未確認，不能直接作為支持依據 |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | 未知 | 60 | 鼻竇內視鏡手術中，比較靜脈輸注 esmolol 與 lidocaine 對術後恢復品質的影響，與 oxymetazoline 關聯間接 |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | 終止 | 3 | Kovanaze（tetracaine 加 oxymetazoline）鼻噴劑對比 articaine 用於上顎牙髓麻醉，屬牙科用途，非鼻腔疾病 |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | 完成 | 16 | 比較 cocaine、lidocaine/xylometazoline 與生理食鹽水的鼻內鎮痛，所用藥物是另一種咪唑啉類，並非 oxymetazoline |
| [NCT07173023](https://clinicaltrials.gov/study/NCT07173023) | NA | 尚未招募 | 30 | 比較兩種後鼻孔閉鎖的手術技術，oxymetazoline 至多是圍手術期輔助用藥 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | 臨床生理研究 | Annals of the New York Academy of Sciences | 36 位受試者，以化學感覺誘發電位、心理物理測驗與聲學鼻量測法，評估感冒（急性鼻炎）對嗅覺功能的影響 |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | 世代研究 | Journal of Plastic Surgery and Hand Surgery | 以聲學鼻量測法比較單側完全唇顎裂修補後兒童與對照組的鼻腔通氣 |
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | 動物實驗 | Annals of Otology, Rhinology & Laryngology | 在兔急性細菌性上頜竇炎模型中，評估 oxymetazoline 滴鼻對局部組織防禦的影響 |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | 病例系列 | American Journal of Rhinology & Allergy | 遺傳性出血性毛細血管擴張症的鼻部毛細血管擴張，以內視鏡引導 coblation 治療的手術技巧 |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | 病例報告 | Global Pediatric Health | 9 歲男童鼻硬結症罕見病例，介紹典型鼻塞表現與組織學診斷 |

---

## 香港上市資訊

香港共有 13 張許可證，以下列出 5 張主要許可證。資料中的核准適應症與劑型欄位皆為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-51462 | OXY-NASE PAEDIATRIC NASAL SOL 0.025% | TAISHO PHARMACEUTICAL (HK) LTD |
| HK-43745 | LOGICIN RAPID RELIEF NASAL SPRAY 0.05% | ASPEN PHARMACARE ASIA LIMITED |
| HK-52653 | OXY-NASE NASAL DROPS 0.05%W/V | TAISHO PHARMACEUTICAL (HK) LTD |
| HK-58133 | NASAL RELIEF SPRAY 0.05% | WILSON TRADING COMPANY LIMITED |
| HK-51937 | OXY-NASE NASAL SPRAY 0.05% | TAISHO PHARMACEUTICAL (HK) LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。香港衛生署仿單的警語與禁忌尚未取得。

依現有評估與文獻，可作為參考的重點有：
- **長期使用**：可能出現反彈性鼻充血（藥物性鼻炎）。
- **心血管**：對心血管疾病等易感族群可能有影響。
- **藥物交互作用**：文獻提示與 MAO 抑制劑有臨床上相關的交互作用（PMID 36425231）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 「鼻腔疾病」與 oxymetazoline 已知的鼻減充血用途高度吻合，且該藥在香港已有多張鼻用製劑許可證。
- 但直接支持證據偏弱：相關試驗多為手術或檢查前的輔助用藥、樣本小，或未直接使用 oxymetazoline。高 TxGNN 分數也主要反映既有用途，所以視為「現有用途的確認」，不算新用途發現。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌（目前是阻斷性資料缺口，無法進入安全性篩選）。
- 補上 DrugBank 的作用機轉資料。
- 釐清原適應症：許可證的核准適應症文字為空，需回頭確認。
- 確認 NCT00562120 等待查證的試驗所用藥物與終點，才能作為證據等級的依據。
- 為長期使用訂定監測與用藥指引（避免反彈性充血），並關注心血管疾病患者及 MAOI 併用者。

**其他預測適應症（供參考）：**
- **頭痛疾患 (Headache Disorder)**：TxGNN 分數 99.04%，證據等級 L3，僅有小型回顧性研究（PMID 31919839，tetracaine 加 oxymetazoline 用於偏頭痛持續狀態）與個案觀察，無法分離 oxymetazoline 單獨的貢獻，建議視為研究問題。
- **急性喉咽炎 (Acute Laryngopharyngitis)**：TxGNN 分數 99.95%，無任何試驗或文獻，且鼻黏膜局部給藥難以到達喉咽部，建議暫緩 (Hold)。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

