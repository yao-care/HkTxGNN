---
layout: default
title: Pseudoephedrine
parent: 高證據等級 (L1-L2)
nav_order: 731
evidence_level: L2
indication_count: 3
---

# Pseudoephedrine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **3** 個
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

# Pseudoephedrine：從（原適應症未登錄）到鼻腔疾病

## 一句話總結

Pseudoephedrine（偽麻黃鹼）是一種間接擬交感神經藥物，常見於鼻塞減充血與感冒複方產品，但本次資料中未登錄原適應症。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效。
目前檢索到 **19 個臨床試驗登記**和 **7 篇文獻**，但其中只有少數直接測試 pseudoephedrine。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知藥理，Pseudoephedrine 是間接擬交感神經藥物，會透過 α 腎上腺素受體引起鼻黏膜血管收縮，減輕黏膜腫脹與鼻塞。

鼻腔疾病（如過敏性鼻炎、鼻竇炎）的核心症狀之一就是黏膜充血腫脹，因此機轉上高度吻合。

需要注意：這項預測（分數 0.997）較像是模型重新發現一個**已知的減充血用途**，而不是全新的老藥新用。由於輸入資料沒有登錄原適應症，建議先對照香港許可證的實際核准內容，確認這個用途是否已在仿單上。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00804687](https://clinicaltrials.gov/study/NCT00804687) | Phase 2 | 完成 | 53 | 隨機、安慰劑對照、三向交叉試驗，在環境暴露艙中比較 JNJ-39220675、pseudoephedrine 與安慰劑對過敏性鼻炎的療效 |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | 完成 | 160 | 雙盲隨機試驗，比較光纖鼻咽喉鏡前使用局部麻醉或減充血劑的舒適度；減充血劑可能是局部用藥，而非口服 pseudoephedrine |
| [NCT00517946](https://clinicaltrials.gov/study/NCT00517946) | N/A | 完成 | 21 | 以 MRI 評估抗過敏藥物對鼻腔結構的影響（方法學研究），未確認有 pseudoephedrine 組 |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | 完成 | 21 | H3 受體拮抗劑對過敏原誘發鼻塞的影響（四向交叉），測試的是其他藥物 |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | 未知 | 60 | 比較 esmolol 與 lidocaine 輸注對鼻竇手術術後恢復品質的影響，與本藥關聯間接 |
| [NCT04645511](https://clinicaltrials.gov/study/NCT04645511) | N/A | 招募中 | 120 | 氣球鼻竇擴張術對慢性鼻竇炎的安慰劑對照研究，為手術試驗，未測試本藥 |
| [NCT03979209](https://clinicaltrials.gov/study/NCT03979209) | Phase 1 | 完成 | 16 | 高容量 mometasone 鼻沖洗的皮質醇抑制研究，屬不同藥物 |
| [NCT05494346](https://clinicaltrials.gov/study/NCT05494346) | N/A | 招募中 | 101 | 含精油的海水減充血噴劑用於急性鼻炎鼻塞，為醫材性質的產品 |
| [NCT06580210](https://clinicaltrials.gov/study/NCT06580210) | N/A | 招募中 | 114 | 機械式海水減充血噴劑用於急性鼻炎鼻塞，為醫材性質的產品 |
| [NCT01886768](https://clinicaltrials.gov/study/NCT01886768) | N/A | 未知 | 212 | 比較單、雙棉片鼻腔麻醉用於經鼻內視鏡，涉及鼻腔減充血 |

> 直接涉及 pseudoephedrine 的只有 NCT00804687（Phase 2，已完成）。其餘多為間接相關或不同介入。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | 臨床比較研究 | Am J Rhinol | 以聲學鼻量測法比較 phenylpropanolamine 與 d-pseudoephedrine 的口服與局部鼻減充血效果 |
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy Asthma Proc | 非過敏性鼻炎的分類與症狀（鼻塞、流鼻水、打噴嚏）回顧 |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | 動物實驗 | Am J Rhinol Allergy | 貓鼻塞模型中，loratadine 加 montelukast 有減充血效果，並評估 d-pseudoephedrine 加 desloratadine |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | 動物實驗 | J Pharmacol Toxicol Methods | 慢性犬鼻塞模型的藥理特性，用於研究減充血藥的作用機轉 |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | 動物實驗 | Am J Rhinol | 以聲學鼻量測法建立犬鼻塞模型 |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | 動物實驗 | Am J Rhinol | 對豚草過敏犬的過敏性鼻塞模型 |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | 動物實驗 | J Pharmacol Exp Ther | 選擇性 α2c 腎上腺素受體促效劑在鼻塞動物模型中的評估 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-50092 | PSEUDOEPHEDRINE HYDROCHLORIDE (ZHEJIANG APELOA) | SHIN KEE DRUG CO LTD |
| HK-62991 | NASAFED TABLETS 60MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-64853 | VASOCEDINE PSEUDOEPHEDRINE TABLETS 60MG | JACOBSON MEDICAL (HONG KONG) LIMITED |
| HK-50328 | VICODRINE TAB 60MG | VICKMANS LABORATORIES LTD |
| HK-44693 | LOGICIN SINUS TAB 60MG | ASPEN PHARMACARE ASIA LIMITED |

共 20 張許可證，上表列出 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有一個已完成的 Phase 2 隨機對照試驗（NCT00804687）直接納入 pseudoephedrine，加上 2001 年的臨床比較研究，支持其鼻減充血作用，因此證據等級為 L2。但這個用途本來就是已知的減充血機轉，並非全新發現。同時，仿單的警語與禁忌資料缺漏，屬於阻擋性缺口，所以只能附條件推進。

**若要推進需要：**
- 從香港衛生署下載並解析仿單，取得核准適應症、警語與禁忌症（目前許可證的適應症欄位皆為空）
- 補充 DrugBank 的作用機轉資料
- 確認 NCT00804687 的 pseudoephedrine 組別與主要結果
- 釐清「鼻腔疾病」與香港現行核准適應症的差異，判斷是否算新適應症

**其他預測適應症：**
- 急性喉咽炎：僅有模型預測、無試驗與文獻（L5），建議 Hold。
- 過敏性蕁麻疹：文獻多為抗組織胺，與 pseudoephedrine 僅間接關聯（L4），建議 Hold。

> 本報告結果僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

