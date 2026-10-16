---
layout: default
title: Sodium Citrate
parent: 僅模型預測 (L5)
nav_order: 820
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Sodium Citrate：預測新適應症為乳突性結膜炎 (Papillary Conjunctivitis)（證據等級 L5）。原適應症：消化性潰瘍、胃食道逆流、消化不良、咽炎、感冒、鼻炎等"
---

# Sodium Citrate
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

# Sodium Citrate：從消化道與上呼吸道症狀到乳突性結膜炎（預測）

## 一句話總結

Sodium Citrate（檸檬酸鈉）是常見的鹼化劑與緩衝劑，原本用於消化性潰瘍、胃食道逆流、消化不良，以及咽炎、感冒、鼻炎等上呼吸道症狀。
TxGNN 模型預測它可能對**乳突性結膜炎 (Papillary Conjunctivitis)** 有效，但目前**沒有臨床試驗和文獻**支持，僅屬模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 消化性潰瘍、胃食道逆流、消化不良、咽炎、感冒、鼻炎等（香港許可證未載明適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 乳突性結膜炎 (Papillary Conjunctivitis) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，檸檬酸鈉是鹼化劑與緩衝劑，在胃酸相關疾病中可中和酸性，在香港也常見於含祛痰成分的複方止咳糖漿，以及血液濾過液和口服補水鹽中。

乳突性結膜炎屬眼部過敏或刺激性疾病，與原本的消化道、上呼吸道適應症在藥理上缺乏明確關聯，也沒有已知的眼部或抗過敏機轉。模型的高分很可能來自知識圖譜中的網絡鄰近性，而不是實際的生物學證據。

其他預測適應症的情況類似：

| 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|-----------|-----------|---------|------|
| 鼻腔疾病 (Nasal Cavity Disease) | 99.95% | L5 | 可能與原本的鼻炎、感冒適應症相近，僅為網絡推論 |
| 急性喉咽炎 (Acute Laryngopharyngitis) | 99.94% | L5 | 可能與原本的咽炎、感冒相近，無臨床支持 |
| 胃部疾病 (Stomach Disease) | 99.89% | L4 | 範圍廣泛，與現有適應症重疊，不是獨立的再利用機會 |
| 胃切除後症候群 (Postgastrectomy Syndrome) | 99.79% | L5 | 無文獻，無已建立機轉 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（乳突性結膜炎），目前無相關文獻。

以下為排名第 4 的「胃部疾病」所檢索到的文獻，內容多屬間接證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25316860](https://pubmed.ncbi.nlm.nih.gov/25316860/) | 2014 | 社區隨機對照試驗 | J Infect Dis | 以緩衝液中和胃酸，探討是否改善口服小兒麻痺疫苗的免疫反應 |
| [1959368](https://pubmed.ncbi.nlm.nih.gov/1959368/) | 1991 | 臨床比較 | Crit Care Med | 比較 sucralfate 與 ranitidine 用於加護病房壓力性潰瘍預防及續發肺炎 |
| [7086102](https://pubmed.ncbi.nlm.nih.gov/7086102/) | 1982 | 臨床生理研究 | J Clin Gastroenterol | 多數有症狀的十二指腸潰瘍患者，對胃十二指腸酸化並未出現潰瘍型疼痛 |
| [1777551](https://pubmed.ncbi.nlm.nih.gov/1777551/) | 1991 | 製劑研究 | Aliment Pharmacol Ther | azapropazone 加入葡萄糖與檸檬酸鈉後，大鼠胃黏膜損傷減少 |
| [27163639](https://pubmed.ncbi.nlm.nih.gov/27163639/) | 2016 | 體外研究 | Biochem Biophys Res Commun | 3-溴丙酮酸合併檸檬酸鈉抑制糖解，誘導胃癌細胞凋亡 |
| [26708213](https://pubmed.ncbi.nlm.nih.gov/26708213/) | 2016 | 體外／動物研究 | Oncol Rep | 兩者合併抑制糖解並抑制胃癌原位移植瘤生長 |
| [29115645](https://pubmed.ncbi.nlm.nih.gov/29115645/) | 2018 | 動物研究 | Oncol Rep | 以 18F-FDG PET/CT 搭配胃癌原位異種移植模型評估糖解標靶治療 |

上述文獻多為間接證據：檸檬酸鈉常作為緩衝劑或製劑輔料，或與其他藥物合併用於癌細胞實驗，並不直接支持檸檬酸鈉單獨治療胃部疾病。

---

## 香港上市資訊

香港共有 20 張有效的單一成分許可證，以下列出 5 張主要許可證。資料中未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-28241 | SOD CITRATE SOLN 3.13%（B. Braun） | — | — |
| HK-65289 | REGIOCIT SOLUTION FOR HAEMOFILTRATION | — | — |
| HK-49787 | BENA EXPECTORANT | — | — |
| HK-47398 | DIPHENHYDRAMINE COMP LINCTUS | — | — |
| HK-64418 | ORALITE NATURAL ORAL REHYDRATION SALTS | — | — |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容，僅供參考）：高血壓、胰臟炎、腎上腺皮質功能不全（含 Addison 病）、良性前列腺肥大、無尿、橫紋肌溶解症、高血鈣、腎鈣質沉著症、冠狀動脈疾病、心肌梗塞、腎功能不全、代謝性酸中毒、隅角閉鎖型青光眼、先天性腎上腺增生等。
- **藥物交互作用**：資料庫共有 100 筆交互作用紀錄，其中前 20 筆顯示：
  - **重大 (Major)**：氫氧化鋁 (Aluminum hydroxide)
  - **中等 (Moderate)**：Doxycycline、Minocycline、Tetracycline、Levofloxacin、Acetylsalicylic acid、鐵劑、Ephedrine、Pseudoephedrine、Rosuvastatin、Acalabrutinib
  - **輕微 (Minor)**：磺醯脲類降血糖藥（Glipizide、Glyburide、Chlorpropamide、Tolbutamide 等）、Lactulose、Misoprostol

香港仿單的警語與禁忌尚未取得，詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測（乳突性結膜炎）沒有任何臨床試驗或文獻，且檸檬酸鈉缺乏已知的眼部或抗過敏機轉，高分僅反映知識圖譜的網絡關係，證據等級為 L5。
- 其餘預測不是缺乏證據，就是與現有適應症重疊（如胃部疾病），並非獨立的再利用機會。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，檢驗預測的生物學合理性
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 以文獻與臨床試驗登記資料再次檢索乳突性結膜炎、鼻腔及咽喉疾病的直接證據
- 評估眼用或局部給藥途徑是否可行；目前給藥途徑相容性資料尚缺
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

