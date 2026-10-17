---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Etonogestrel：預測新適應症為閉經 (Amenorrhea)（證據等級 L5）。原適應症：香港許可證未登載適應症文字（依其劑型與藥理類別，一般為避孕）"
monitor_inn: "ETONOGESTREL"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "blunt duct adenosis of breast", "apocrine adenosis of breast", "benign mammary dysplasia"]
---

# Etonogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Etonogestrel：從避孕到閉經（Amenorrhea）

## 一句話總結

Etonogestrel 是一種黃體素（progestin），以皮下植入劑形式用於避孕（香港已有 IMPLANON NXT 上市）。
TxGNN 模型預測它可能對**閉經 (amenorrhea)** 有效，但目前**沒有相關臨床試驗**，僅有 **1 篇文獻**，且該文獻與本藥及閉經無關，因此實質上只有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未登載適應症文字（依其劑型與藥理類別，一般為避孕） |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，etonogestrel 是黃體素類藥物，可抑制排卵並使子宮內膜變薄。

需要特別注意：閉經是此植入劑已知的**藥理副作用**（黃體素暴露的藥效學結果），並不是治療目標。TxGNN 的高分很可能反映「藥物類別與月經改變」之間的關聯，而非真正的再利用證據。若要說有潛在價值，較合理的方向是處理異常或大量出血，而非「治療閉經」本身。

本次預測的其他候選為乳房纖維囊腫、鈍性導管腺病、大汗腺腺病及良性乳腺發育不良（分數 99.2%–99.6%）。這些同樣沒有臨床試驗或文獻支持。乳房疼痛本身是此植入劑已知的不良反應，反而不利於這類適應症。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT 研究計畫書（無關） | Trials | BIO101 用於預防 COVID-19 肺炎患者呼吸惡化的試驗計畫，與 etonogestrel 及閉經皆無關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68214 | IMPLANON NXT IMPLANT 68MG（廠商：ORGANON HONG KONG LIMITED） | 植入劑 | 無登載資料 |

---

## 安全性考量

- **知識圖譜標示的相關疾病（非仿單內容）**：TxGNN 知識圖譜顯示 etonogestrel 與下列疾病存在禁忌關聯，包括高血壓、癲癇、焦慮與神經症、紫質症、腎臟疾病、肝臟疾病、膽囊疾病、系統性紅斑狼瘡、氣喘、糖尿病（含酮酸中毒）、高三酸甘油脂血症與高脂血症、女性乳癌、血栓性靜脈炎、偏頭痛、冠狀動脈疾病及肥胖。這些僅供參考，實際禁忌請以仿單為準。
- **藥物交互作用**：資料庫共記錄 100 筆交互作用，列出的皆為中度。主要包括：
  - 降血糖藥物：acarbose、metformin、glimepiride、chlorpropamide、alogliptin、saxagliptin、canagliflozin、dapagliflozin、empagliflozin、albiglutide、dulaglutide、semaglutide，以及多種胰島素（aspart、degludec、detemir、glargine、glulisine）
  - 其他：aprepitant、clarithromycin、linaclotide

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型預測（L5），沒有臨床試驗，唯一的文獻也與本藥無關。
- 閉經是此藥的預期副作用而非治療目標，乳房相關預測則與已知的乳房疼痛不良反應相抵觸。

**若要推進需要：**
- 取得香港衛生署的仿單，確認警語、禁忌與核准適應症
- 補充 DrugBank 的作用機轉資料
- 重新界定臨床問題（例如以植入劑相關異常出血的管理取代「治療閉經」），並進行針對性文獻檢索
- 針對乳房良性病變，需有前臨床或臨床研究佐證後才考慮重新評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

