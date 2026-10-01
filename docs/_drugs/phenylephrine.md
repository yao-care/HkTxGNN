---
layout: default
title: Phenylephrine
parent: 僅模型預測 (L5)
nav_order: 678
evidence_level: L5
indication_count: 3
---

# Phenylephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Phenylephrine：從 α1 腎上腺素促效劑到鼻腔疾病

## 一句話總結

Phenylephrine（苯腎上腺素）是 α1 腎上腺素受體促效劑，香港已有鼻噴劑、注射劑與眼藥水等多張許可證。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，目前有 **8 個臨床試驗**和 **8 篇文獻**，但多為間接證據，且此預測可能只是重現既有的鼻充血用途。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未提供（香港許可證的核准適應症文字皆為空白） |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2（僅有 1 個已完成的 Phase 2 RCT，且該試驗是否使用 phenylephrine 尚未確認） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。不過 Phenylephrine 屬於 α1 腎上腺素促效劑，這是已知的藥理類別。它會讓鼻黏膜血管收縮，帶來去充血與減少出血的效果。

臨床上它也常與局部麻醉劑合併使用，例如 co-phenylcaine（lidocaine 加 phenylephrine），用於鼻腔內視鏡等鼻部檢查與處置前。因此「鼻腔疾病」的預測在機轉上相當合理。

**需特別注意：** 鼻部去充血本來就是 phenylephrine 的既有用途。這個高分預測可能只是反映現有用途，而不是真正的新適應症。在視為新適應症之前，應先對照香港許可證的核准適應症。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | 完成 | 21 | 季節性過敏性鼻炎患者在鼻過敏原激發後，以雙盲交叉設計評估 H3 受體拮抗劑對鼻塞的影響。試驗標題被截斷，是否以 phenylephrine 為受試藥物無法確認 |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | 不適用 | 完成 | 106 | 比較 co-phenylcaine（含 phenylephrine）噴霧與霧化給藥，用於硬式鼻內視鏡檢查前。屬給藥方式比較，並非單測 phenylephrine 療效 |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | 完成 | 16 | 比較古柯鹼、lidocaine/xylometazoline 與生理食鹽水的鼻內鎮痛效果。未明顯涉及 phenylephrine，樣本也很小 |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | 不適用 | 未知 | 120 | 比較經鼻內視鏡與外路淚囊鼻腔吻合術。Phenylephrine 至多是術中血管收縮劑 |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | 完成 | 20 | 比較 oxymetazoline 與 epinephrine 在鼻竇手術前對出血量與視野的影響，僅可視為同類血管收縮劑的參考 |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | 終止 | 3 | Kovanaze（tetracaine/oxymetazoline）鼻噴劑對比 articaine 的牙科麻醉，使用不同血管收縮劑，無實質參考價值 |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | 進行中（停止招募） | 60 | 內視鏡鼻竇手術中靜脈輸注 esmolol 對比 lidocaine，非局部鼻用介入，與 phenylephrine 無直接關聯 |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | 撤回 | 0 | Kovanaze 對比 articaine 的牙科麻醉試驗，從未收案，無可用證據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | RCT | Int J Clin Pract | 98 位病人在可撓式鼻咽內視鏡前使用 cophenylcaine 或安慰劑噴霧，兩組疼痛與不適皆輕微，無顯著差異 |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT | PLoS One | 局部使用 tranexamic acid 對鼻竇手術出血與術野的影響。測試藥物不是 phenylephrine，僅屬背景參考 |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | 實驗與臨床研究 | Vestn Otorinolaringol | 評估含 phenylephrine 的 Polydexa 噴霧（含抗生素與類固醇）在急性鼻竇炎的安全性與療效 |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | 回顧 | Vestn Otorinolaringol | 針對鼻與鼻竇發炎疾病的病理機轉導向治療，指出藥物應減輕黏膜充血與水腫 |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | 世代研究 | Vestn Otorinolaringol | 使用含 phenylephrine 的 Polydexa 噴霧後，以內視鏡評估慢性鼻腔疾病的黏膜狀態 |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | 世代研究 | Int J Pediatr Otorhinolaryngol | 以聲波鼻量測法評估腺樣體與扁桃腺切除術後的鼻腔與鼻咽幾何變化 |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | 體外研究 | Clin Otolaryngol | 在體外探討各種鼻科用藥對纖毛擺動頻率的影響 |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | 個案報告 | Arch Ophthalmol | 淚囊鼻腔吻合術前鼻內使用古柯鹼出現毒性反應，其中一位病人對鼻內 phenylephrine 也出現額外反應 |

---

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。資料中的核准適應症文字皆為空白，劑型為依品名判斷。

| 許可證號 | 品名 | 劑型（依品名） | 廠商 |
|---------|------|------|------|
| HK-62569 | DURACON NASAL SPRAY 0.5%W/V | 鼻噴劑 | WELL FAVOURED LTD |
| HK-66214 | PHENYLALPHA SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 500MCG/10ML | 預充填注射液 | HONG KONG MEDICAL SUPPLIES LTD |
| HK-68282 | PHENYLEPHRINE SINTETICA SOLUTION FOR INJECTION OR INFUSION 10MG/1ML | 注射／輸注液 | MEKIM LTD |
| HK-49280 | NOARL AS FOR CHILDREN EYE DROPS 0.1% | 眼藥水 | SATO PHARMACEUTICAL (HK) CO LTD |
| HK-30148 | MINIMS PHENYLEPHRINE HCL EYE DROPS 2.5% | 眼藥水 | BAUSCH & LOMB (HK) LTD |

---

## 安全性考量

- **藥物交互作用**：資料庫查詢未找到記錄。
- **個案報告提示**：1980 年的個案報告指出，古柯鹼會阻斷兒茶酚胺再攝取並增強交感神經作用。因此古柯鹼與 phenylephrine 等擬交感神經藥物併用，或用於高血壓心血管疾病患者時有風險（PMID 7378007）。

其餘警語與禁忌症資料缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 機轉合理，且 phenylephrine 作為鼻用血管收縮劑已有臨床使用，還有含 phenylephrine 的製劑在鼻科研究中使用。
- 但直接以 phenylephrine 為單一受試藥的試驗很少，TxGNN 高分預測也可能只是反映既有用途。
- 香港許可證缺少核准適應症，目前的安全性資料也不足，因此只能有條件推進。

**若要推進需要：**
- 取得香港衛生署仿單，確認鼻腔疾病是否已是核准適應症。這能判斷此預測是新適應症還是既有用途。
- 補齊警語與禁忌症，並取得 DrugBank 的作用機轉資料。
- 確認 NCT00562120 的完整試驗設計，看是否真的包含 phenylephrine。
- 針對特定鼻腔疾病（如過敏性鼻炎、鼻竇炎）設計單一成分、對照明確的試驗。

**其他預測適應症（暫不推進，皆為 Hold）：**
- **急性喉咽炎 (Acute Laryngopharyngitis)**：分數 99.97%，證據等級 L5，無任何臨床試驗與文獻佐證。
- **三叉自主神經性頭痛 (Trigeminal Autonomic Cephalalgia)**：分數 99.30%，證據等級 L4。現有文獻多為以 phenylephrine 滴眼測量瞳孔反應的生理與診斷研究，屬於藥理探針用途，並非治療效益證據。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

