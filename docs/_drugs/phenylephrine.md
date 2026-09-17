---
layout: default
title: Phenylephrine
parent: 高證據等級 (L1-L2)
nav_order: 581
evidence_level: L2
indication_count: 3
---

# Phenylephrine
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

# Phenylephrine：從減充血用途到鼻腔疾病 (Nasal Cavity Disease)

## 一句話總結

Phenylephrine 是選擇性 α1-腎上腺素受體促效劑，臨床上常作為鼻黏膜血管收縮劑（減充血）使用，但本次評估未取得其正式登記的原始適應症紀錄。TxGNN 模型預測它與**鼻腔疾病 (Nasal Cavity Disease)** 高度相關（score 99.97%），目前有 **8 個臨床試驗**與 **8 篇文獻**可供參考，但多數為手術輔助用途的間接佐證，直接治療效力證據有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未記錄（原始適應症與 MOA 皆為資料缺口，詳見下方說明） |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 正式的作用機轉摘要（Data Gap）。根據 evidence pack 內的機轉推論，Phenylephrine 為選擇性 α1-腎上腺素受體促效劑，作用於鼻黏膜血管平滑肌造成血管收縮，減少黏膜充血與腫脹——這是藥理學上已被廣泛認識的去充血機轉。

值得注意的是，本次資料集的 `original_indications` 為空（資料缺口），因此無法確認「鼻腔疾病」對這個藥物而言究竟是全新的老藥新用方向，還是本來就已知的臨床用途（例如作為 OTC 鼻用減充血劑）。多數支持證據（如 co-phenylcaine 鼻噴劑、鼻內視鏡術前使用、鼻竇手術術中止血）是把 phenylephrine 當作**局部血管收縮輔助劑**使用，而非治療慢性鼻腔疾病本身，這點在解讀 TxGNN 高分時需要留意。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | NA | 完成 | 106 | Co-phenylcaine（含 phenylephrine+lidocaine）鼻噴劑用於硬式鼻內視鏡檢查前，兼具局部麻醉與減充血效果，改善鼻腔視野與患者舒適度 |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | 完成 | 21 | H3 受體拮抗劑對季節性過敏性鼻炎鼻過敏原激發後鼻塞的影響，以聲學鼻腔測量法評估鼻塞程度 |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | NA | 未知 | 120 | 鼻內視鏡淚囊鼻腔造口術比較，術中常規使用 phenylephrine 收縮鼻黏膜血管以改善手術視野（間接證據） |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | 完成 | 20 | 比較 Oxymetazoline 與 Epinephrine（同類非 phenylephrine）用於鼻竇手術前，評估出血量與視野 |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | 完成 | 16 | 比較 Cocaine 與 Lidocaine/Xylometazoline 用於清醒經鼻插管的鼻內麻醉，未涉及 phenylephrine |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | 進行中未招募 | 60 | Esmolol 與 Lidocaine 靜脈輸注對功能性鼻竇內視鏡手術恢復品質的影響，機轉關聯薄弱 |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | 終止 | 3 | Kovanaze（tetracaine/oxymetazoline）鼻噴劑 vs Articaine 用於上顎牙科麻醉，樣本過小 |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | 撤回 | 0 | 同上 Kovanaze 系列試驗，未招募即撤回，無可用數據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | RCT | Int J Clin Pract | Cophenylcaine 噴劑 vs 安慰劑用於軟式鼻咽鏡檢查，雙盲隨機試驗，兩組疼痛與不適感無顯著差異 |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT | PLoS One | 局部 Tranexamic acid 對慢性鼻竇炎功能性內視鏡手術出血與視野品質的影響（間接相關） |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Review | Vestnik otorinolaringologii | 含 phenylephrine 的 Polydexa 鼻噴劑（複方）用於外科術後及局部抗生素治療後鼻腔慢性疾病之鑑別診斷 |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik otorinolaringologii | 鼻及副鼻竇發炎性疾病的病理生理導向治療原則，強調需減輕黏膜充血與腫脹 |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case Report | Arch Ophthalmol | 淚囊鼻腔造口術中使用鼻內 cocaine 併發 phenylephrine 反應之毒性案例報告 |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Cohort | Vestnik otorinolaringologii | 含 phenylephrine 之 Polydexa 噴劑用於急性鼻竇炎的安全性與有效性實驗暨臨床評估 |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | Cohort | Clin Otolaryngol | 體外研究多種鼻科常用藥物對纖毛擺動頻率之劑量依賴效應 |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Cohort | Int J Pediatr Otorhinolaryngol | 腺樣體/扁桃腺切除術後以聲學鼻腔測量法評估鼻腔與鼻咽幾何構造變化 |

---

## 香港上市資訊

目前於香港無許可證登記（未上市）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 藥理機轉明確（α1 促效劑、黏膜血管收縮），且有 A 級證據（NCT03380715, n=106 已完成）及一篇 tier 1 RCT（PMID 15854186）支持鼻腔局部應用的安全性與耐受性，TxGNN 分數極高（99.97%）。
- 但多數證據為「手術/檢查輔助用途」而非「疾病治療」，且原始適應症與正式 MOA 資料缺失，無法排除此預測只是重新發現既有已知用途；安全性資料（仿單警語、禁忌、DDI）完全空缺，屬於 Blocking 等級缺口，暫不能進入正式安全性初評（S1）。

**若要推進需要：**
- 補齊仿單警語/禁忌資料（DG001，Blocking）
- 補齊正式 MOA 來源，如 DrugBank API 查詢（DG002）
- 釐清 `original_indications` 是否本已涵蓋鼻腔相關適應症，以確認是否屬於真正的老藥新用
- 補充 DDI 資料以支援後續安全性評估

**補充：** 同批預測中另有兩個候選——急性喉咽炎（acute laryngopharyngitis, L5, Hold，無任何臨床試驗或文獻）與三叉自律神經性頭痛（trigeminal autonomic cephalalgia, L4, Hold）。後者雖有 16 篇文獻，但內容幾乎全為以 phenylephrine 作為瞳孔藥理學診斷探針（鑑別 Horner's syndrome），並非治療性介入證據，兩者證據強度均不足以支持推進。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

