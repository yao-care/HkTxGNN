---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Durvalumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Durvalumab：從非小細胞肺癌到前列腺尿道尿路上皮癌

---

## 一句話總結

Durvalumab（品牌名 IMFINZI）是 AstraZeneca 研發的抗 PD-L1 單株抗體，全球已核准用於非小細胞肺癌、小細胞肺癌、膽道癌及尿路上皮癌等多種惡性腫瘤，惟香港目前尚未上市。TxGNN 模型針對此藥物共預測 **10 項罕見腫瘤亞型**，最高排名為**前列腺尿道尿路上皮癌（Prostatic Urethra Urothelial Carcinoma）**（TxGNN 分數 99.98%）；跨所有預測適應症共收錄 **4 個臨床試驗**及 **1 篇文獻**，最具發展潛力的適應症為**子宮頸內膜癌（L3，Proceed with Guardrails）**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症（全球） | 非小細胞肺癌、小細胞肺癌、膽道癌、尿路上皮癌（香港未獲批） |
| 最高排名預測新適應症 | 前列腺尿道尿路上皮癌 (Prostatic Urethra Urothelial Carcinoma) |
| TxGNN 預測分數（第 1 名） | 99.98% |
| 最佳證據等級 | L3（子宮頸內膜癌；膀胱尿路上皮癌肉瘤樣亞型） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold（最高排名預測）；Proceed with Guardrails（子宮頸內膜癌） |

---

## 各預測適應症總覽

| 排名 | 適應症（中文） | 適應症（英文） | TxGNN 分數 | 證據等級 | 臨床試驗數 | 文獻數 | 建議決策 |
|------|-------------|-------------|-----------|---------|-----------|--------|---------|
| 1 | 前列腺尿道尿路上皮癌 | Prostatic Urethra Urothelial Carcinoma | 99.98% | L5 | 0 | 0 | Hold |
| 2 | 腎盂肉瘤樣移行細胞癌 | Kidney Pelvis Sarcomatoid Transitional Cell Carcinoma | 99.98% | L4 | 1（間接） | 0 | Research Question |
| 3 | 浸潤性膀胱尿路上皮癌肉瘤樣亞型 | Infiltrating Bladder Urothelial Carcinoma Sarcomatoid Variant | 99.98% | L3 | 2 | 0 | Research Question |
| 4 | 腎盂乳頭狀尿路上皮癌 | Renal Pelvis Papillary Urothelial Carcinoma | 99.98% | L5 | 0 | 0 | Hold |
| 5 | 子宮韌帶腺癌 | Uterine Ligament Adenocarcinoma | 99.92% | L5 | 0 | 0 | Hold |
| 6 | 子宮頸內膜癌 | Endocervical Carcinoma | 99.91% | L3 | 2 | 1 | **Proceed with Guardrails** |
| 7 | 宮頸腺樣囊性癌 | Adenoid Cystic Carcinoma of the Cervix Uteri | 99.91% | L5 | 0 | 0 | Hold |
| 8 | 子宮韌帶漿液性腺癌 | Uterine Ligament Serous Adenocarcinoma | 99.91% | L5 | 0 | 0 | Hold |
| 9 | 宮頸黏液腺癌印戒細胞亞型 | Signet Ring Cell Variant Cervical Mucinous Adenocarcinoma | 99.90% | L5 | 0 | 0 | Hold |
| 10 | 宮頸腸型黏液腺癌 | Intestinal Variant Cervical Mucinous Adenocarcinoma | 99.90% | L5 | 0 | 0 | Hold |

---

## 為什麼這個預測合理？

Durvalumab 是一種高親和力、選擇性的 IgG1κ 單株抗體，靶向 PD-L1（Programmed Death-Ligand 1）。透過阻斷 PD-L1 與 PD-1 及 CD80 的交互作用，Durvalumab 解除腫瘤微環境中的免疫抑制訊號，使 CD8+ 細胞毒性 T 細胞重新啟動抗腫瘤活性。

**TxGNN 預測的 10 項適應症可分為兩大機轉群**：

1. **尿路上皮癌亞型（排名 1–4）**：前列腺尿道、腎盂、膀胱等不同解剖部位的罕見組織學亞型。尿路上皮癌（UC）普遍具有 PD-L1 高表現（文獻報告 40–70%），其中肉瘤樣變異型因上皮間質轉化（EMT）特徵及豐富免疫浸潤，理論上對 PD-L1 阻斷更為敏感。Durvalumab 在廣義尿路上皮癌（膀胱癌）已有全球核准先例，知識圖譜推斷延伸至這些罕見亞型具備明確機轉基礎。

2. **婦科惡性腫瘤亞型（排名 5–10）**：宮頸及子宮韌帶等部位的各種腺癌亞型。其中**子宮頸內膜癌**（HPV 相關型）PD-L1 表現率可達 30–70%，且同類藥物 Pembrolizumab 已獲 FDA 核准用於 PD-L1 陽性或 MSI-H 宮頸癌，提供強力的類別效應（class effect）支持。反之，腺樣囊性癌（MYB-NFIB 融合、免疫「冷」腫瘤）及印戒細胞亞型（HPV 相關性低、PD-L1 誘導弱）的機轉匹配度相對較低。

> 注意：本 Evidence Pack 中作用機轉（MOA）原始資料存在資料缺口（DG002），以上分析係基於 Durvalumab 已發表之藥理學文獻及全球核准資料。

---

## 臨床試驗證據

### 尿路上皮癌相關試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 適用排名 | 主要發現 |
|---------|------|------|------|---------|---------|
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | 提早終止 | 7 | 排名 3 | 開放標籤研究，直接評估 Durvalumab + 新輔助化療（含鉑類）於變異組織學膀胱癌（含肉瘤樣亞型）。設計相關性最高，但因收案嚴重不足提早終止，無法得出療效結論，終止原因未揭露 |
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | 招募完成（進行中） | 54 | 排名 2、3 | Durvalumab + Tremelimumab 術前先導研究，針對不適合順鉑的高風險肌層浸潤型尿路上皮癌，提供廣義 UC 安全性訊號；腎盂肉瘤樣 TCC 為可能子族群，屬間接支持 |

### 婦科癌症相關試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 適用排名 | 主要發現 |
|---------|------|------|------|---------|---------|
| [NCT04065269](https://clinicaltrials.gov/study/NCT04065269) | Phase 2 | 招募完成（進行中） | 174 | 排名 6 | ATARI 試驗：評估 ATR 抑制劑 Ceralasertib（AZD6738）單用或聯合 Olaparib/Durvalumab，對象為依 ARID1A 基因狀態分層的復發婦科癌症（含子宮頸相關），宮頸內膜癌為婦科亞組之一 |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | 已完成 | 20 | 排名 6 | 低分次立體定向放射治療 + Durvalumab + Tremelimumab，針對復發/轉移性宮頸、陰道及外陰癌；已完成並提供 Durvalumab 於宮頸癌情境下的初步安全性確認 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 適用排名 | 主要發現 |
|------|-----|------|------|---------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | 排名 6 | 子宮頸小細胞神經內分泌癌（SCNECC）分子基礎與治療進展系統性回顧；指出現有臨床試驗不足，治療沿用肺部 SCNE 準則，並探索包含免疫治療在內的新型療法於此罕見 HPV 相關宮頸癌亞型的可行性 |

---

## 香港上市資訊

Durvalumab 目前在香港**尚未上市**，衛生署藥物資料庫中無任何已批准許可證記錄。若需在香港使用，須透過衛生署「未經批准藥物的申請」（Unlicensed Drug Application）機制，並提交原廠（AstraZeneca）全球核准資料及仿單。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（抗 PD-L1 單株抗體，IgG1κ；非傳統細胞毒性藥物） |
| 骨髓抑制風險 | 低（主要不良事件為免疫相關不良事件 irAE，並非直接骨髓毒性） |
| 致吐性分級 | 低 |
| 監測項目 | 肝功能（ALT / AST / 膽紅素）、甲狀腺功能（TSH / FT4）、腎功能（肌酸酐 / eGFR）、空腹血糖 / HbA1c、CBC（含分類計數）、腎上腺功能（有臨床指徵時） |
| 處置防護 | 依一般生物製劑靜脈輸注規範操作；發生嚴重 irAE（≥Grade 3）時需立即暫停給藥並啟動高劑量皮質類固醇治療方案 |

---

## 安全性考量

安全性資訊請參考原廠仿單（AstraZeneca IMFINZI 全球說明書）。

根據全球已核准藥品資料，Durvalumab 主要安全性風險為**免疫相關不良事件（irAE）**，常見包含：

- **免疫性肺炎**（Immune-mediated Pneumonitis）
- **免疫性肝炎**（Immune-mediated Hepatitis）
- **免疫性內分泌疾病**（甲狀腺炎、垂體炎、腎上腺功能不全）
- **免疫性腸炎**（Immune-mediated Colitis）
- **免疫性腎炎**（Immune-mediated Nephritis）

---

## 結論與下一步

### 整體決策摘要

| 預測適應症 | 最終建議 |
|-----------|---------|
| 子宮頸內膜癌 | **Proceed with Guardrails** |
| 膀胱尿路上皮癌肉瘤樣亞型 | **Research Question** |
| 腎盂肉瘤樣移行細胞癌 | **Research Question** |
| 其餘 7 項適應症 | **Hold** |

---

### 優先適應症：子宮頸內膜癌

**決策：Proceed with Guardrails**

**理由：**
子宮頸內膜癌（HPV 相關型）具 PD-L1 高表現特性（30–70%），與 Durvalumab 作用機轉高度吻合；Pembrolizumab 在 PD-L1+/MSI-H 宮頸癌的 FDA 核准提供強力的類別效應支持，機轉轉化合理性強。現有 1 個已完成的 Phase 1 試驗（NCT03452332）提供安全性基礎，加上大規模進行中 Phase 2 試驗（NCT04065269，174 人），構成 L3 等級證據。

### 研究問題（Research Question）適應症：膀胱/腎盂尿路上皮癌肉瘤樣亞型

**決策：Research Question**

**理由：**
NCT03912818 直接針對膀胱尿路上皮癌肉瘤樣亞型設計，但因收案 7 例即提早終止，資料幾乎空白；NCT02812420 為廣義 UC 先導研究，屬間接支持。肉瘤樣亞型理論上對 PD-L1 阻斷更敏感，有明確科學問題值得深入探索，但現有數據不足以支持直接推進。

---

**若要推進需要：**
- 補填資料缺口 DG001（香港仿單警語/禁忌）及 DG002（MOA 原始文件），以完成 S1 安全性初評
- 取得 NCT03912818 提早終止的完整原因及已收案 7 例的初步安全性資料
- 評估香港/台灣宮頸癌患者的 PD-L1 表現率及 HPV 基因型分布（尤其是 HPV16/18 相關宮頸腺癌），確認本地患者族群適用性
- 聯繫 NCT04065269 研究團隊，評估加入宮頸內膜癌亞組分析的可行性
- 向香港衛生署諮詢「未經批准藥物申請」或「個別患者特殊使用申請」的監管路徑
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

